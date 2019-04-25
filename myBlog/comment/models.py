from django.db import models
from blog.models import User, Article
# Create your models here.


class CommentManager(models.Manager):
    """
    评论管理类类
    """
    def create_comment(self, user, article, content):
        comment = self.model()
        comment.user = user
        comment.article = article
        comment.content = content
        return comment

    def create_save_comment(self, user, article, content):
        comment = self.create(user=user, article=article, content=content)
        return comment


class Comment(models.Model):
    """定义评论类"""
    # 评论人
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 评论文章
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # 评论内容
    content = models.TextField()
    # 评论时间
    comment_time = models.DateTimeField(auto_now_add=True)
    manager = CommentManager()

    def show_user(self):
        return self.user

    def show_article(self):
        return self.article

    def show_comment_time(self):
        return self.comment_time

    show_user.short_description = "评论人"
    show_article.short_description = "文章标题"
    show_comment_time.short_description = "发布时间"

