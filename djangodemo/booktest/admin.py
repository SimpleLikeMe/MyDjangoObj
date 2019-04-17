from django.contrib import admin
from .models import *


# Register your models here.


class OrdersInline(admin.StackedInline):
    model = Orders
    # 关联个数
    extra = 1


class UserAdmin(admin.ModelAdmin):
    # 列表显示字段
    # list_display = ["name", "addr"]
    list_display = ["name", "addr", "skill"]
    # 过滤器，指定过滤规则
    list_filter = ["name", "addr"]
    # 搜索框，支持模糊查询
    search_fields = ["name", "addr"]
    # 分页显示
    list_per_page = 3
    # 再添加书的时候可以额外添加用户
    # inlines = [OrdersInline]



class OrdersAdmin(admin.ModelAdmin):
    # 列表显示字段
    list_display = ["user_id", "goods_id"]
    # 过滤器，指定过滤规则
    list_filter = ["user_id", "goods_id"]
    # 搜索框，支持模糊查询
    search_fields = ["user_id", "goods_id"]
    # 分页显示
    list_per_page = 3



class GoodsAdmin(admin.ModelAdmin):
    # 列表显示字段
    list_display = ["name", "price"]
    # 过滤器，指定过滤规则
    list_filter = ["name", "price"]
    # 搜索框，支持模糊查询
    search_fields = ["name", "price"]
    # 分页显示
    list_per_page = 3


admin.site.register(User, UserAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Orders, OrdersAdmin)
