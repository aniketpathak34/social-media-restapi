from datetime import timedelta
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import UserProfile, Post, Like, Comment
from .serializers import UserProfileSerializer, PostSerializer, LikeSerializer, CommentSerializer
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView


DUMMY_USERS = {
    1: {'username': 'dummy', 'password': 'dummy_password'},
    # Add more users as needed
}

class CustomTokenObtainPairView(TokenObtainPairView):
    pass

# Rest of your views and code...


@api_view(['POST'])
def authenticate_user(request):
    # Perform dummy authentication (replace with your actual authentication logic)
    username = request.data.get('username')
    password = request.data.get('password')

    # Example dummy authentication logic
    if username == 'dummy' and password == 'dummy_password':
        # Call the custom token obtain view to generate and return a JWT token
        view = CustomTokenObtainPairView.as_view()
        return view(request).data
    else:
        return Response({'error': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, id):
    user_to_follow = get_object_or_404(User, id=id)
    user_profile = request.user.userprofile

    if user_to_follow != request.user and user_to_follow not in user_profile.followers.all():
        user_profile.followers.add(user_to_follow)
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, id):
    user_to_unfollow = get_object_or_404(User, id=id)
    user_profile = request.user.userprofile

    if user_to_unfollow != request.user and user_to_unfollow in user_profile.followers.all():
        user_profile.followers.remove(user_to_unfollow)
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user_profile = request.user.userprofile
    serializer = UserProfileSerializer(user_profile)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request, id):
    post = get_object_or_404(Post, id=id, user=request.user)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, id):
    post = get_object_or_404(Post, id=id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if created:
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, id):
    post = get_object_or_404(Post, id=id)
    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Like.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_comment(request, id):
    post = get_object_or_404(Post, id=id)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, post=post)
        comment_data = serializer.data

        # Retrieve the updated post data with comments
        updated_post = Post.objects.get(id=id)
        post_serializer = PostSerializer(updated_post)

        response_data = {
            'post': post_serializer.data,
            'comment': comment_data
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_single_post(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post)
    likes_count = Like.objects.filter(post=post).count()

    post_serializer = PostSerializer(post)
    comments_serializer = CommentSerializer(comments, many=True)

    post_data = {
        'post': post_serializer.data,
        'comments': comments_serializer.data,
        'likes_count': likes_count
    }

    return Response(post_data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_posts(request):
    posts = Post.objects.filter(user=request.user).order_by('-created_at')
    post_data = []

    for post in posts:
        comments_count = Comment.objects.filter(post=post).count()
        likes_count = Like.objects.filter(post=post).count()

        post_serializer = PostSerializer(post)
        post_data.append({
            'post': post_serializer.data,
            'comments_count': comments_count,
            'likes_count': likes_count
        })

    return Response(post_data)

