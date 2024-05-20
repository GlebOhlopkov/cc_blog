from django.urls import path

from post.views import PostCreateAPIView, PostRetrieveAPIView, PostUpdateAPIView, PostDeleteAPIView

app_name = 'post'

urlpatterns = [
    path('create/', PostCreateAPIView.as_view(), name='post_create'),
    path('<int:pk>/', PostRetrieveAPIView.as_view(), name='post_detail'),
    path('update/<int:pk>/', PostUpdateAPIView.as_view(), name='post_update'),
    path('delete/<int:pk>/', PostDeleteAPIView.as_view(), name='post_delete'),
]
