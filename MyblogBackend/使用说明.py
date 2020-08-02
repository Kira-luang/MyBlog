# 1.图片路劲
'''
需要修改图片路劲的话,搜索FileField,找到to_representation方法进行修改,修改url的赋值

request = self.context.get('request', None)
url = 'http://127.0.0.1:8000/static/img/' + url
return url
'''

# 2.需要的插件
'''
Redis:
pip install django-redis
pip install django-redis-cache

Cerely:
pip install django-celery-results

django-cors-headers:
pip install django-cors-headers

Pillow:
pip install Pillow

django-rest-multiple-models:
pip install django-rest-multiple-models
'''
