# djangorestapi/urls.py

from django.urls import path
from .views import (
    authenticate_user,
    follow_user,
    unfollow_user,
    user_profile,
    create_post,
    delete_post,
    like_post,
    unlike_post,
    add_comment,
    get_single_post,
    get_all_posts,
    CustomTokenObtainPairView,
)

urlpatterns = [
    path('api/authenticate/', authenticate_user),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/follow/<int:id>/', follow_user),
    path('api/unfollow/<int:id>/', unfollow_user),
    path('api/user/', user_profile),
    path('api/posts/', create_post),
    path('api/delete/<int:id>/', delete_post),
    path('api/like/<int:id>/', like_post),
    path('api/unlike/<int:id>/', unlike_post),
    path('api/comment/<int:id>/', add_comment),
    path('api/posts/<int:id>/', get_single_post),
    path('api/all_posts/', get_all_posts),
]
