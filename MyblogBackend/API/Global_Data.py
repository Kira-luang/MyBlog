# 每一页的返回的数据总数
from django.core.cache import caches

PER_PAGE = 10

# 主页的ID
INDEX_ID = 1

# 用户未登录不能允许访问的路劲

GET_AUTHORITY_PATH = {'/api/img/', }
POST_AUTHORITY_PATH = {'/api/message/', '/api/aticlemessage/', '/api/addagree/', '/api/messageagree/', '/api/articleagree/(?P<pk>\d+)'}
# '/api/token/'验证用户token是否过期
TEST_AUTHORITY = {'/api/token/'}

# 全局缓存
CACHE = caches['default']

ACTIVATE_URL = 'http://127.0.0.1:8000/api/activate/'

# 激活后跳转的URL
FONTEND_URL = 'http://127.0.0.1:8888/login'
