from django.contrib import admin
from .models import *
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    """评论管理类"""
    # 显示列表
    list_display = ['id', 'show_user', 'show_article', 'show_comment_time']
    # 添加过滤项
    list_filter = ['id', 'user', 'article', 'comment_time']
    # 添加搜索框
    search_fields = ['id', 'user', 'article']
    # 分页显示
    list_per_page = 3


# 注册comment
admin.site.register(Comment, CommentAdmin)
