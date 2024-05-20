from django.contrib import admin

from comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Comment Model for Admin-panel
    """

    list_display = ('author', 'post', 'text', 'created_at', 'last_correct')
