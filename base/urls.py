from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers

from base.api import views as apiviews
from . import views


router = routers.DefaultRouter()
# router.register('posts', apiviews.PostViewSet)
router.register('myusers', apiviews.UserViewSet)

users_router = routers.NestedDefaultRouter(router, 'myusers', lookup='myuser')
users_router.register('posts', apiviews.PostViewSet, basename='myuser-posts')

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"), 

    path('update-user/', views.updateUser, name="update-user"),
    path('topics/', views.topicsPage, name="topics"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('create-post/', views.create_post_view, name="create-post"),
    path('post/<uuid:post_id>/', views.post_detail_view, name='post_detail'),

    path('user/posts/<uuid:user_id>/', views.view_user_posts, name='view_user_posts'),
      path('user/posts/<uuid:post_id>/edit/', views.edit_post, name='edit_post'),

    # path('', views.index, name='home'),

    path('api/', include(router.urls)),
    path('api/', include(users_router.urls)),
    
    # path('posts/<str:pk>/', views.post, name='post'),
]
