from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import add_comment, edit_comment, delete_comment
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from django.urls import path
from . import views


urlpatterns = [
    # Create a new comment under a specific post
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
    
    # Update a specific comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit-comment'),
    
    # Delete a specific comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
]


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]


urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]


urlpatterns = [
    path('post/<int:post_id>/comment/new/', add_comment, name='add-comment'),
    path('comment/<int:comment_id>/edit/', edit_comment, name='edit-comment'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete-comment'),
]

urlpatterns = [
    path('search/', views.search_posts, name='search_posts'),
    path('tags/<str:tag_name>/', views.posts_by_tag, name='posts_by_tag'),
]


