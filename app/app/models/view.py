from django.db import models
from django.utils import timezone
from . import Flower
from django.conf import settings

class View(models.Model):
    flower = models.ForeignKey(Flower, related_name='views', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, db_constraint=False)
    view_at = models.DateTimeField(auto_now_add=True)
