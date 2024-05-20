from django.urls import path

from comment.views import CommentCreateAPIView, CommentRetrieveAPIView, CommentUpdateAPIView, CommentDeleteAPIView

app_name = 'comment'

urlpatterns = [
    path('create/', CommentCreateAPIView.as_view(), name='comment_create'),
    path('<int:pk>/', CommentRetrieveAPIView.as_view(), name='comment_detail'),
    path('update/<int:pk>/', CommentUpdateAPIView.as_view(), name='comment_update'),
    path('delete/<int:pk>/', CommentDeleteAPIView.as_view(), name='comment_delete'),
]
