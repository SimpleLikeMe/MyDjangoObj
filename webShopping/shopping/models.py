from django.db import models

# Create your models here.


class ProductKind(models.Model):
    name = models.CharField(max_length=20)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    describe = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    kind = models.ForeignKey('ProductKind', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

