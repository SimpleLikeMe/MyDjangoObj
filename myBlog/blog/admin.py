from django.contrib import admin

from .models import *
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    """创建用户表管理类"""
    # 显示的列的列表
    list_display = ['show_account', 'show_nickname', 'show_email', 'show_integral', 'show_register_time']
    # 添加过滤项
    list_filter = ['account', 'email', 'integral', 'register_time']
    # 添加搜索框，支持模糊查询
    search_fields = ['account', 'nickname', 'email', 'integral', 'register_time']
    # 分页显示
    list_per_page = 5


class ArticleAdmin(admin.ModelAdmin):
    """创建用户表管理类"""
    # 显示的列的列表
    list_display = ['id', 'show_title', 'show_read_count', 'show_publish_time']
    # 添加过滤项
    list_filter = ['id', 'title', 'read_count', 'publish_time']
    # 添加搜索框，支持模糊查询
    search_fields = ['id', 'title', 'read_count', 'publish_time']
    # 分页显示
    list_per_page = 5


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


# 注册表单交给管理界面管理
admin.site.register(User, UserAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleKind)
admin.site.register(ArticleTag)
