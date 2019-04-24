from .models import *
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['account', 'password', 'nickname', 'email', 'gender', 'age', 'integral', 'describe']
        labels = {
            'account': '账号',
            'password': '密码',
            'nickname': '昵称',
            'email': '邮箱',
            'gender': '性别',
            'age': '年龄',
            'integral': '积分',
            'describe': '个人简介',
        }
        widgets = {
            'password': forms.widgets.PasswordInput()
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        labels = {
            'content': '评论：',
        }
        widgets = {
            'password': forms.widgets.TextInput(attrs={'class': 'form-control', 'style': 'width:500px'})
        }
