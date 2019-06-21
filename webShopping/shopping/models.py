from django.db import models

# Create your models here.


class ProductFeatured(models.Model):
    name = models.CharField(max_length=20)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ProductKind(models.Model):
    name = models.CharField(max_length=20)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    name = models.CharField(max_length=15)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ProductColor(models.Model):
    name = models.CharField(max_length=20)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ProductComposition(models.Model):
    name = models.CharField(max_length=15)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ProductStyle(models.Model):
    name = models.CharField(max_length=15)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ProductProperty(models.Model):
    name = models.CharField(max_length=15)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ProductAvailability(models.Model):
    name = models.CharField(max_length=30)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=30)
    price = models.FloatField()
    stock = models.IntegerField()
    describe = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    kind = models.ManyToManyField('ProductKind')
    featured = models.ManyToManyField('ProductFeatured', null=True, blank=True)
    is_wishlist = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Hat(Product):
    # 尺寸
    size = models.ForeignKey('ProductSize', on_delete=models.CASCADE, null=True, blank=True)
    # 颜色
    color = models.ForeignKey('ProductColor', on_delete=models.CASCADE, null=True, blank=True)
    # 材料
    composition = models.ForeignKey('ProductComposition', on_delete=models.CASCADE, null=True, blank=True)
    # 类型
    style = models.ManyToManyField('ProductStyle')
    # 属性
    property = models.ForeignKey('ProductProperty', on_delete=models.CASCADE, null=True, blank=True)
    # 生产厂商
    availability = models.ForeignKey('ProductAvailability', on_delete=models.CASCADE, null=True, blank=True)


class HatImage(models.Model):
    name = models.CharField(max_length=20)
    src = models.ImageField(upload_to='hat')
    product = models.ForeignKey('Hat', on_delete=models.CASCADE)


class Bag(Product):
    # 尺寸
    size = models.ForeignKey('ProductSize', on_delete=models.CASCADE, null=True, blank=True)
    # 颜色
    color = models.ForeignKey('ProductColor', on_delete=models.CASCADE, null=True, blank=True)
    # 材料
    composition = models.ForeignKey('ProductComposition', on_delete=models.CASCADE, null=True, blank=True)
    # 类型
    style = models.ManyToManyField('ProductStyle')
    # 属性
    property = models.ForeignKey('ProductProperty', on_delete=models.CASCADE, null=True, blank=True)
    # 生产厂商
    availability = models.ForeignKey('ProductAvailability', on_delete=models.CASCADE, null=True, blank=True)


class BagImage(models.Model):
    name = models.CharField(max_length=20)
    src = models.ImageField(upload_to='bag')
    product = models.ForeignKey('Bag', on_delete=models.CASCADE)


class Watch(Product):
    # 尺寸
    size = models.ForeignKey('ProductSize', on_delete=models.CASCADE, null=True, blank=True)
    # 颜色
    color = models.ForeignKey('ProductColor', on_delete=models.CASCADE, null=True, blank=True)
    # 材料
    composition = models.ForeignKey('ProductComposition', on_delete=models.CASCADE, null=True, blank=True)
    # 类型
    style = models.ManyToManyField('ProductStyle')
    # 属性
    property = models.ForeignKey('ProductProperty', on_delete=models.CASCADE, null=True, blank=True)
    # 生产厂商
    availability = models.ForeignKey('ProductAvailability', on_delete=models.CASCADE, null=True, blank=True)


class WatchImage(models.Model):
    name = models.CharField(max_length=20)
    src = models.ImageField(upload_to='watch')
    product = models.ForeignKey('Watch', on_delete=models.CASCADE)


class Glasses(Product):
    # 尺寸
    size = models.ForeignKey('ProductSize', on_delete=models.CASCADE, null=True, blank=True)
    # 颜色
    color = models.ForeignKey('ProductColor', on_delete=models.CASCADE, null=True, blank=True)
    # 材料
    composition = models.ForeignKey('ProductComposition', on_delete=models.CASCADE, null=True, blank=True)
    # 类型
    style = models.ManyToManyField('ProductStyle')
    # 属性
    property = models.ForeignKey('ProductProperty', on_delete=models.CASCADE, null=True, blank=True)
    # 生产厂商
    availability = models.ForeignKey('ProductAvailability', on_delete=models.CASCADE, null=True, blank=True)


class GlassesImage(models.Model):
    name = models.CharField(max_length=20)
    src = models.ImageField(upload_to='glasses')
    product = models.ForeignKey('Glasses', on_delete=models.CASCADE)


class Shoe(Product):
    # 尺寸
    size = models.ForeignKey('ProductSize', on_delete=models.CASCADE, null=True, blank=True)
    # 颜色
    color = models.ForeignKey('ProductColor', on_delete=models.CASCADE, null=True, blank=True)
    # 材料
    composition = models.ForeignKey('ProductComposition', on_delete=models.CASCADE, null=True, blank=True)
    # 类型
    style = models.ManyToManyField('ProductStyle')
    # 属性
    property = models.ForeignKey('ProductProperty', on_delete=models.CASCADE, null=True, blank=True)
    # 生产厂商
    availability = models.ForeignKey('ProductAvailability', on_delete=models.CASCADE, null=True, blank=True)


class ShoeImage(models.Model):
    name = models.CharField(max_length=20)
    src = models.ImageField(upload_to='shoe')
    product = models.ForeignKey('Shoe', on_delete=models.CASCADE)


class Order(models.Model):
    product = models.ForeignKey(Hat, on_delete=models.CASCADE)
    quantity = models.IntegerField()

