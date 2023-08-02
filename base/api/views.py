from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from base.api.serializers import PostSerializer, UserSerializer
from base.models import Post, User



#Api Viewsets for generating API endpoints
class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer

    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Post.objects.filter(user_id=self.kwargs['myuser_pk'])
    
    def get_serializer_context(self):

        return {'user_id': self.kwargs['myuser_pk']}
    
    def get_permissions(self):
        if self.request.method == 'GET':

            return [AllowAny()]
        return [IsAuthenticated()]
    

class UserViewSet(ModelViewSet):

    queryset = User.objects.prefetch_related('posts').all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'patch']

    permission_classes = [AllowAny]

