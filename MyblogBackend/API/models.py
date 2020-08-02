from django.db import models

# Create your models here.


class ColumnName(models.Model):
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=38)
    keyword = models.CharField(max_length=56)
    description = models.CharField(max_length=156)
    path = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'ColumnName'


class Article(models.Model):
    title = models.CharField(max_length=38)
    keyword = models.CharField(max_length=56)
    description = models.CharField(max_length=156)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    reads = models.IntegerField(default=10)
    agree = models.IntegerField(default=5)
    thumbnail = models.ImageField(upload_to='%Y%m%d/thumbnail', default='default.jpg')
    is_delete = models.BooleanField(default=False)
    column = models.ForeignKey('ColumnName', on_delete=models.CASCADE)
    Author = models.CharField(max_length=18, default='admin')
    ownername = models.CharField(max_length=18, null=True)
    next = models.IntegerField(null=True, blank=True)
    last = models.IntegerField(null=True, blank=True)
    discuss_count = models.IntegerField(default=0)

    class Meta:
        db_table = 'Article'


class Image(models.Model):
    bigImg = models.ImageField(upload_to='%Y%m%d/bigimg')
    name = models.CharField(max_length=38)
    alt = models.CharField(max_length=38)

    class Meta:
        db_table = 'Image'


class ArticleMessage(models.Model):
    content = models.CharField(max_length=80)
    agree = models.IntegerField(default=0)
    disagree = models.IntegerField(default=0)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'ArticleMessage'


class User(models.Model):
    username = models.CharField(max_length=18, unique=True)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=32, null=True, blank=True)
    headimg = models.ImageField(upload_to='%Y%m%d/image', default='headimg.png')
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'User'


class Message(models.Model):
    content = models.CharField(max_length=80)
    agree = models.IntegerField(default=2)
    disagree = models.IntegerField(default=0)
    column = models.ForeignKey('ColumnName', on_delete=models.SET_NULL, default=6, null=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'Message'


class MessageAgree(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    message = models.ForeignKey('Message', on_delete=models.CASCADE)
    agree = models.IntegerField(default=0)

    class Meta:
        db_table = 'MessageAgree'
        unique_together = ('user', 'message')


class ArticleMessageAgree(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    articleMessage = models.ForeignKey('ArticleMessage', on_delete=models.CASCADE)
    agree = models.IntegerField(default=0)

    class Meta:
        db_table = 'ArticleMessageAgree'
        unique_together = ('user', 'articleMessage')
