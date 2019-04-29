from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class BorrowHistoryManage(models.Manager):
    def crate_borrow_history(self, user, book):
        return self.create(user=user, book=book)


class User(models.Model):
    account = models.CharField(max_length=15, blank=True)
    password = models.CharField(max_length=60, blank=True)
    name = models.CharField(max_length=15, blank=True)
    email = models.EmailField(null=True, blank=True)
    college = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    isbn = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=15)
    publisher = models.CharField(max_length=30)
    publish_date = models.DateField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class BorrowHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_time = models.DateTimeField(auto_now_add=True)
    return_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    manage = BorrowHistoryManage()


class Picture(models.Model):
    name = models.CharField(max_length=20)
    path = models.ImageField(upload_to='index')
    index = models.SmallIntegerField(unique=True)


class Message(models.Model):
    title = models.CharField(max_length=30)
    content = HTMLField()

    def __str__(self):
        return self.title

