from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from . import Comment
from django.conf import settings

class CommentLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, db_constraint=False)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_likes')
    like = models.BooleanField(default=False)
    liked_at = models.DateTimeField(auto_now=True)