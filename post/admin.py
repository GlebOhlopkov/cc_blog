from django.urls import reverse
from django.utils.html import format_html

from django.contrib import admin

from post.models import Post


class PostAdmin(admin.ModelAdmin):
    """
    Post Model for Admin-panel
    """

    list_display = ('title', 'text', 'image', 'author_link', 'created_at', 'last_correct', )
    list_filter = ('created_at',)

    def author_link(self, obj):
        link = reverse("admin:users_user_change", args=[obj.author.id])
        return format_html('<a href="{}">{}</a>', link, obj.author)

    author_link.allow_tags = True
    author_link.short_description = 'Author (Link)'


admin.site.register(Post, PostAdmin)
