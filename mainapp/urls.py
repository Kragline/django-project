from django.urls import path
from .views import *


urlpatterns = [
    path('', PostListView.as_view(), name = 'home'),
    path('post-detail/<int:pk>/', PostDetailsView.as_view(), name = 'detailview'),
    path('add-post/', AddPostView.as_view(), name='add'),
    path('post-detail/edit/<int:pk>', UpdatePostView.as_view(), name = 'update'),
    path('post-detail/delete/<int:pk>', DeletePostView.as_view(), name = 'delete'),
    path('like/<int:pk>', LikeWiew, name = 'like'),
    path('category/<str:cats>', CategoryView, name = 'category'),
    path('search', search_posts, name = 'search'),
]