from urllib.parse import urlsplit , urljoin

from rest_framework import serializers
from API.models import ColumnName , Article , Image , Message , User , ArticleMessage , ArticleMessageAgree , \
    MessageAgree


class ColumnNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColumnName
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class ArticleMessageSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    user_headimg = serializers.ImageField(source='user.headimg', read_only=True)
    class Meta:
        model = ArticleMessage
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'headimg', 'id', 'email']


class MessageSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    user_headimg = serializers.ImageField(source='user.headimg', read_only=True)
    class Meta:
        model = Message
        fields = '__all__'


class ArticleMessageAgreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleMessageAgree
        fields = '__all__'


class MessageAgreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageAgree
        fields = '__all__'