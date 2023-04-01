from . import views
from django.urls import path
from .views import (
    PostList,
    PostDetail,
    PostCreate,
    PostUpdate
)

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/new/', PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
]