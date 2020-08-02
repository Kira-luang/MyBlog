# coding=utf-8
from django.urls import path , re_path

from API import views

urlpatterns = [
    # 栏目增加和查询
    path('columns/' , views.ColumnsViews.as_view()) ,
    # 文章增加和查询
    path('article/' , views.ArticleViews.as_view()) ,
    # 文章图片增加和查询
    path('img/' , views.ImgViews.as_view()) ,
    # 用户注册和登陆
    path('users/' , views.UsersViews.as_view()) ,
    # 文章留言增加和查询
    path('aticlemessage/' , views.ArticleMessageViews.as_view()) ,
    # 留言板的留言查询和添加
    path('message/' , views.MessageViews.as_view()) ,

    # 栏目获取所有文章信息
    re_path(r'column/(?P<pk>\d+)' , views.ColumnViews.as_view()),
    # 单个文章删除,获取以及修改操作
    re_path(r'detail/(?P<pk>\d+)' , views.DetatilViews.as_view()) ,
    # 获取所有栏目/某个栏目的文章数
    path('articlecount/' , views.ArticlesCountViews.as_view()) ,
    # 获取/更新/删除单个栏目对象
    path('singlecolumn/' , views.SingleColumnViews.as_view()) ,
    # 获取文章上一篇和下一篇
    re_path('lastnext/(?P<pk>\d+)' , views.LastNextViews.as_view()) ,
    # 验证token是否有效
    re_path('confirm/' , views.ConfirmViews.as_view()) ,
    # 获取总的用户数和留言板的评论数
    re_path('usermessage/' , views.UserMessageViews.as_view()) ,
    # 文章留言点赞功能
    re_path('addagree/' , views.AddArticleAgreeViews.as_view()) ,
    # 栏目留言点赞功能
    re_path('messageagree/' , views.AddMessageAgreeViews.as_view()) ,
    # 获取某篇文章留言的用户数和评论数
    re_path('userarticlemsg/(?P<pk>\d+)' , views.UserArticleMsgViews.as_view()),
    # 获取某篇文章留言
    re_path('articlemessage/(?P<pk>\d+)' , views.ArticleMsgViews.as_view()),
    # 文章点赞功能
    re_path('articleagree/(?P<pk>\d+)' , views.ArticleAgreeViews.as_view()),
    # 用户激活功能
    re_path('activate/(?P<pk>.+)' , views.ActivateUserViews.as_view()) ,
]