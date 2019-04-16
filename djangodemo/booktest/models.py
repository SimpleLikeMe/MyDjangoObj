from django.db import models

# Create your models here.


class User(models.Model):
    """
    创建用户类与数据库中的用户表对应
    """
    name = models.CharField(max_length=20)
    addr = models.CharField(max_length=30)
    register_time = models.DateTimeField(auto_now_add=True)


class Goods(models.Model):
    """
    创建商品类
    """
    name = models.CharField(max_length=20)
    price = models.FloatField()


class Orders(models.Model):
    """
    创建订单类
    """
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    goods_id = models.ForeignKey('Goods', on_delete=models.CASCADE)
    num = models.IntegerField()
