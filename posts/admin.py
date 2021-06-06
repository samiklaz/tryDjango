from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "timestamp"]
    list_display_links = ["title"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)


