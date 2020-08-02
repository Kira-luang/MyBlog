import uuid
from time import sleep

from celery import shared_task
from django.core.mail import send_mail

from API.Global_Data import ACTIVATE_URL , CACHE
from MyblogBackend.settings import EMAIL_HOST_USER


@shared_task  # 异步装饰器,使该函数变为异步执行
def celery_sendemail(user_email, userid):
    subject = '用户激活'  # 邮件标题
    message = 'Hello'  # 文档
    from_email = EMAIL_HOST_USER  # 邮件来源地址
    recipient_list = [user_email , ]  # 接收邮件地址
    uid = uuid.uuid4().hex  # 创建激活码
    activateURL = ACTIVATE_URL+uid
    CACHE.set(uid, userid, timeout=300)
    html_message = '<h1>请点击以下链接激活邮箱</h1><p><a href="{}">{}</a></p>'.format(activateURL, activateURL)  # html文档
    send_mail(subject , message , from_email , recipient_list=recipient_list , html_message=html_message)
    # 当使用html_message后,便只展现html_message的内容,所以message内容可随意写,只用来作占位符