# coding=utf-8
# Create your views here.
import re
import uuid


from django.contrib.auth.hashers import make_password , check_password
from django.http import HttpResponsePermanentRedirect , HttpResponse
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework import status , views
from rest_framework.generics import ListCreateAPIView , CreateAPIView, ListAPIView

from API import tasks
from API.Global_Data import PER_PAGE , INDEX_ID , CACHE, FONTEND_URL
from API.paginators import Paginator
from API.serializers import ColumnNameSerializer , UserSerializer , ArticleSerializer , ImageSerializer , \
    ArticleMessageSerializer , MessageSerializer , ArticleMessageAgreeSerializer , MessageAgreeSerializer
from API.models import ColumnName , User , Article , Image , ArticleMessage , Message , ArticleMessageAgree , \
    MessageAgree
from rest_framework.response import Response

from API.tasks import celery_sendemail


class ColumnsViews(ListCreateAPIView):
    queryset = ColumnName.objects.all()
    serializer_class = ColumnNameSerializer


# 文章查询全部与增加功能
class ArticleViews(ListCreateAPIView):
    queryset = Article.objects.filter(is_delete=False)
    serializer_class = ArticleSerializer

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['keyword'] = request.data['title']
        request.data['description'] = request.data['title']
        if request.data.get('keyword' , ''):
            request.data['keyword'] = request.data['keyword']
        if request.data.get('description' , ''):
            request.data['description'] = request.data['description']
        # 获取最后一篇修改上一篇和下一篇
        obj = Article.objects.filter(is_delete=False).order_by('time').reverse().first()
        request.data['last'] = obj.id
        try:
            request.data['ownername'] = ColumnName.objects.get(id=request.data['column']).name
        except:
            return Response(data={'message': '内容不存在'}, status=status.HTTP_404_NOT_FOUND)
        request.data._mutable = False

        # 复制源码序列化输出,修改上一篇文章的next
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        obj.next = serializer.data['id']
        obj.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# 添加照片与查询所有功能
class ImgViews(ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['alt'] = request.data['name']
        request.data._mutable = False
        return super().create(request, *args, **kwargs)


# 实现用户注册登录功能
class UsersViews(CreateAPIView, ObjectMultipleModelAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        # 登陆功能
        if request.data.get('action') == 'login':
            username = request.data.get('username')
            password = request.data.get('password')
            try:
                user = User.objects.get(username=username)
                # 验证通过,返回用户实例与token
                if check_password(password, user.password):
                    uid = uuid.uuid4().hex
                    # 利用ObjectMultipleModelAPIView的list源代码来序列化数据
                    querylist = [{'queryset': User.objects.filter(username=username), 'serializer_class': UserSerializer}]
                    results = self.get_empty_results()
                    for query_data in querylist:
                        self.check_query_data(query_data)
                        queryset = self.load_queryset(query_data , request , *args , **kwargs)
                        # Run the paired serializer
                        context = self.get_serializer_context()
                        data = query_data['serializer_class'](queryset , many=True , context=context).data
                        label = self.get_label(queryset , query_data)
                        # Add the serializer data to the running results tally
                        results = self.add_to_results(data , label , results)
                    formatted_results = self.format_results(results , request)
                    formatted_results.update({'token': uid})
                    # 添加token到缓存(要启动redis要不然会报错)
                    CACHE.set(uid , user.id)
                    return Response(formatted_results)
                else:
                    return Response(data={'message': '密码错误'}, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response(data={'message': '用户未注册'}, status=status.HTTP_404_NOT_FOUND)

        # 这里是执行注册功能
        username = request.data.get('username')
        email = request.data.get('email' , '')
        if not email:
            return Response(data={'message': '邮箱未填写'} , status=status.HTTP_406_NOT_ACCEPTABLE)
        try:
            password = request.data.get('password')
            if not password:
                return Response(data={'message': '密码不能为空'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            password = make_password(password)
            user = User.objects.create(username=username, password=password,
                                       email=email, headimg=request.data.get('headimg'))
            celery_sendemail.delay(email, user.id)
        except:
            return Response(data={'message': '用户已存在'}, status=status.HTTP_400_BAD_REQUEST)
        queryset = User.objects.filter(id=user.id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data)


# 实现增加文章留言和查询全部文章留言
class ArticleMessageViews(ListCreateAPIView):
    queryset = ArticleMessage.objects.all()
    serializer_class = ArticleMessageSerializer

    def post(self, request, *args, **kwargs):
        if request.data.get('token' , None):
            token = request.data.get('token')
            userid = CACHE.get(token)
            try:
                User.objects.get(id=userid)
                request.data._mutable = True
                request.data['user'] = userid
                request.data._mutable = False
            except:
                return Response(data={'message':'无效的token'}, status=status.HTTP_401_UNAUTHORIZED)
            return self.create(request, *args, **kwargs)
        return Response(data={'message': '用户未登陆'} , status=status.HTTP_401_UNAUTHORIZED)

    def perform_create(self, serializer):
        serializer.save()
        article = Article.objects.get(id=serializer.data['article'])
        article.discuss_count += 1
        article.save()


# 实现留言版块的查询和留言功能
class MessageViews(ListCreateAPIView):
    def get(self , request , *args , **kwargs):
        self.serializer_class = MessageSerializer
        page = int(request.query_params.get('page', 1))
        paginator_obj = Paginator(Message.objects.all(), page, PER_PAGE, order_field='time', reverse=True)
        self.queryset = paginator_obj.queryset
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.queryset = Message.objects.all()
        self.serializer_class = MessageSerializer
        if request.data.get('token' , None):
            token = request.data.get('token')
            userid = CACHE.get(token)
            try:
                User.objects.get(id=userid)
                request.data._mutable = True
                request.data['user'] = userid
                request.data._mutable = False
                return self.create(request , *args , **kwargs)
            except:
                return Response(data={'message':'无效的token'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(data={'message': '用户未登陆'} , status=status.HTTP_401_UNAUTHORIZED)


# 栏目内容的获取
class ColumnViews(ObjectMultipleModelAPIView):
    def get(self , request , *args , **kwargs):
        article_list = Article.objects.filter(is_delete=False)
        if kwargs['pk'] != '1':
            column = ColumnName.objects.filter(id=kwargs['pk'])
            if not column:
                return Response(data={'message': '栏目不存在'} , status=status.HTTP_404_NOT_FOUND)
            article_list = article_list.filter(column=kwargs['pk'])
        else:
            article_list = article_list.exclude(column=2)
        # 分页器
        page = int(request.query_params.get('page', 1))
        paginator_obj = Paginator(article_list , page , PER_PAGE , order_field='agree', reverse=True)
        self.paginators = {'count': paginator_obj.count, 'num_pages': paginator_obj.num_pages,
                           'page': paginator_obj.page, 'page_range': paginator_obj.page_range,
                           'perpage': PER_PAGE}
        # 序列化
        self.querylist = [{'queryset': paginator_obj.queryset, 'serializer_class': ArticleSerializer}]
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        querylist = self.get_querylist()
        results = self.get_empty_results()
        for query_data in querylist:
            self.check_query_data(query_data)
            # 获取queryset
            queryset = self.load_queryset(query_data, request, *args, **kwargs)
            # Run the paired serializer
            context = self.get_serializer_context()
            data = query_data['serializer_class'](queryset, many=True, context=context).data
            label = self.get_label(queryset, query_data)

            # Add the serializer data to the running results tally
            results = self.add_to_results(data, label, results)
        formatted_results = self.format_results(results, request)

        formatted_results.update({'paginators': self.paginators})

        return Response(formatted_results)


# 单篇文章查询,更新,删除功能
class DetatilViews(ObjectMultipleModelAPIView, views.APIView):
    def get(self, request, *args, **kwargs):
        article = Article.objects.filter(is_delete=False).filter(id=kwargs['pk'])
        try:
            article_obj = Article.objects.get(id=kwargs['pk'])
        except:
            return Response({'message': '你请求的资源不存在'}, status=status.HTTP_404_NOT_FOUND)
        self.querylist = [{'queryset': article, 'serializer_class': ArticleSerializer}]
        # 阅读量+1
        article_obj.reads += 1
        article_obj.save()
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            obj = Article.objects.get(id=kwargs['pk'])
        except:
            return Response({'message': '访问资源不存在'}, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        action = data.get('action', 'update')
        if action == 'update':
            for key, value in request.data.items():
                setattr(obj , key , value)
        elif action == 'delete':
            '''删除要设置delete,还要修改上一篇文章与下一篇文章的关系'''
            obj.is_delete = True
            if obj.last and obj.next:
                last_obj = Article.objects.get(id=obj.last)
                next_obj = Article.objects.get(id=obj.next)
                last_obj.next, next_obj.last = obj.next, obj.last
                last_obj.save()
                next_obj.save()
            elif obj.last:
                last_obj = Article.objects.get(id=obj.last)
                last_obj.next = None
                last_obj.save()
            elif obj.next:
                next_obj = Article.objects.get(id=obj.next)
                next_obj.last = None
                next_obj.save()
        else:
            return Response({'message': '请求错误'}, status=status.HTTP_403_FORBIDDEN)
        obj.save()
        return Response({'message': '请求成功'})


# 获取所有栏目/某个栏目的文章数
class ArticlesCountViews(views.APIView):
    def get(self, request, *args, **kwargs):
        count = {}
        column_list = request.query_params.get('columnid')
        if column_list:
            column_list = map(lambda x: int(x) , re.findall('\d+' , column_list))
            for column_id in column_list:
                try:
                    if column_id != 1:
                        length = len(Article.objects.filter(column=column_id))
                    else:
                        length = len(Article.objects.all())
                    count[ColumnName.objects.get(id=column_id).name] = length
                except:
                    return Response(data={'message:访问资源不存在'}, status=status.HTTP_404_NOT_FOUND)
        else:
            columns = ColumnName.objects.all()
            for column in columns:
                count[column.name] = len(Article.objects.filter(column=column.id))
            count[ColumnName.objects.get(id=INDEX_ID).name] = len(Article.objects.all())
        return Response(data=count)


# 根据id/path获取单个栏目对象
class SingleColumnViews(views.APIView):
    queryset = ColumnName.objects.all()
    serializer_class = ColumnNameSerializer

    def get(self, request, *args, **kwargs):
        path = request.query_params.get('path')
        id = request.query_params.get('id')
        if path:
            try:
                column = ColumnName.objects.get(path=path)
            except:
                return Response({'message': '没有该页面'} , status=status.HTTP_404_NOT_FOUND)
        elif id:
            try:
                column = ColumnName.objects.get(id=id)
            except:
                return Response({'message': '没有该页面'} , status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': '没有该页面'} , status=status.HTTP_403_FORBIDDEN)
        data = {}
        for key, value in column.__dict__.items():
            if key != '_state':
                data[key] = value
        return Response(data=data)


# 获取文章的上一篇和下一篇
class LastNextViews(ListAPIView):
    serializer_class = ArticleSerializer
    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        self.queryset = Article.objects.all()
        try:
            article = Article.objects.get(id=id)
            if article.is_delete:
                raise Exception
            next_queryset = Article.objects.filter(id=article.next)
            last_queryset = Article.objects.filter(id=article.last)
        except:
            return Response(data={'message':'请求资源不存在'}, status=status.HTTP_403_FORBIDDEN)
        self.queryset = last_queryset | next_queryset
        return self.list(request, *args, **kwargs)


# 验证token是否有效
class ConfirmViews(views.APIView):
    def get(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        if CACHE.get(token):
            return Response(data={'message': 'token有效'})
        return Response(data={'message': '无效token'},status=status.HTTP_401_UNAUTHORIZED)


class UserMessageViews(views.APIView):
    def get(self, request, *args, **kwargs):
        usercount = len(User.objects.all())
        messagecount = len(Message.objects.all())
        return Response(data={'usercount': usercount, 'messagecount': messagecount})


# 文章留言点赞功能
class AddArticleAgreeViews(views.APIView):
    def get_obj(self, request, userid, *args, **kwargs):
        articleMessageID = request.data.get('articleMessage')
        return ArticleMessageAgree.objects.filter(user=userid , articleMessage=articleMessageID).first()

    def changeAgreeCount(self, obj):
        obj = obj.articleMessage
        obj.agree = len(obj.articlemessageagree_set.all().filter(agree=1))
        obj.disagree = len(obj.articlemessageagree_set.all().filter(agree=2))
        obj.save()
        return obj

    def create_obj(self, request, userid, *args, **kwargs):
        is_agree = request.data.get("action", '')
        articleMessage = request.data.get("articleMessage")
        if is_agree == 'disagree':
            agree = 2
        else:
            agree = 1
        user = User.objects.filter(id=userid).filter(is_active=True)
        articleMessage = ArticleMessage.objects.filter(id=articleMessage)
        if not user:
            return Response(data={'message': '未激活用户'}, status=status.HTTP_404_NOT_FOUND)
        if not articleMessage:
            return Response(data={'message': '文章留言不存在'} , status=status.HTTP_404_NOT_FOUND)
        obj = ArticleMessageAgree.objects.create(user=user.first() , agree=agree , articleMessage=articleMessage.first())
        return obj

    def post(self, request, *args, **kwargs):
        token = request.data.get('token')
        userid = CACHE.get(token)
        articleagree = self.get_obj(request, userid, *args, **kwargs)
        # 判断是否已经点过赞
        if articleagree:
            if request.data.get('action') == 'disagree':
                if articleagree.agree == 2:
                    articleagree.agree = 0
                else:
                    articleagree.agree = 2
            else:
                if articleagree.agree == 1:
                    articleagree.agree = 0
                else:
                    articleagree.agree = 1
            articleagree.save()
            obj = self.changeAgreeCount(articleagree)
            return Response(data={'agree': obj.agree, 'disagree': obj.disagree})
        agree_obj = self.create_obj(request, userid, *args, **kwargs)
        if isinstance(agree_obj, Response):
            return agree_obj
        obj = self.changeAgreeCount(agree_obj)
        return Response(data={'agree': obj.agree, 'disagree': obj.disagree})


# 留言版留言点赞功能
class AddMessageAgreeViews(AddArticleAgreeViews):

    def get_obj(self, request, userid, *args, **kwargs):
        messageid = request.data.get('message')
        return MessageAgree.objects.filter(user=userid , message=messageid).first()

    def changeAgreeCount(self, obj):
        obj = obj.message
        obj.agree = len(obj.messageagree_set.all().filter(agree=1))
        obj.disagree = len(obj.messageagree_set.all().filter(agree=2))
        obj.save()
        return obj

    def create_obj(self, request, userid, *args, **kwargs):
        is_agree = request.data.get("action", '')
        message = request.data.get("message")
        if is_agree == 'disagree':
            agree = 2
        else:
            agree = 1
        user = User.objects.filter(id=userid).filter(is_active=True)
        message = Message.objects.filter(id=message)
        if not user:
            return Response(data={'message': '用户不存在'}, status=status.HTTP_404_NOT_FOUND)
        if not message:
            return Response(data={'message': '文章留言不存在'} , status=status.HTTP_404_NOT_FOUND)
        obj = MessageAgree.objects.create(user=user.first() , agree=agree , message=message.first())
        return obj

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserArticleMsgViews(views.APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', '')
        article_messages = ArticleMessage.objects.filter(article=pk)
        users = set()
        if article_messages:
            for article_message in article_messages:
                if article_message.user not in users:
                    users.add(article_message.user_id)
            return Response(data={'messagecount': len(article_messages) , 'usercount': len(users)})
        else:
            return Response(data={'messagecount': 0 , 'usercount': 0})


class ArticleMsgViews(ListAPIView):
    serializer_class = ArticleMessageSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        self.queryset = ArticleMessage.objects.filter(article=pk)
        return self.list(request, *args, **kwargs)


class ArticleAgreeViews(views.APIView):
    serializer_class = ArticleSerializer

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        try:
            article = Article.objects.get(id=pk)
            token = request.data.get('token')
            userid = CACHE.get(token)

            if CACHE.get(userid):
                userid_set = CACHE.get(userid)
                if article.id in userid_set:
                    return Response(data={'message': '重复点赞'}, status=status.HTTP_403_FORBIDDEN)
                else:
                    userid_set.add(article.id)
                    CACHE.set(userid, userid_set)
            else:
                CACHE.set(userid, {article.id, })
            article.agree += 1
            article.save()
            return Response(data={'message': '点赞成功', 'articleAgree': article.agree})
        except:
            return Response(data={'message': '没有该篇文章'}, status=status.HTTP_404_NOT_FOUND)


class ActivateUserViews(views.APIView):
    def get(self, request, *args, **kwargs):
        activate_code = kwargs['pk']
        userid = CACHE.get(activate_code)
        try:
            user = User.objects.get(id=userid)
            user.is_active = True
            user.save()
            return HttpResponsePermanentRedirect(FONTEND_URL)
        except:
            return HttpResponse('用户不存在,请先创建用户')
