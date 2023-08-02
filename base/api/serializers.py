from rest_framework import serializers

from ..models import Post, User

from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
            model = Post
            fields = ['id', 'title', 'body']

    def create(self, validated_data):
          user_id = self.context['user_id']
          return Post.objects.create(user_id=user_id, **validated_data)


#Creating User
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'name', 'password','email']


class UserSerializer(serializers.ModelSerializer):
      
      posts = PostSerializer(many=True, read_only=True)
      class Meta:
            model = User
            fields = ['id', 'username', 'name', 'email',  'posts']            