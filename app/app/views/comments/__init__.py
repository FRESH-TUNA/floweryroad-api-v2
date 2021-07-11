from rest_framework.viewsets import ViewSet
from rest_framework.mixins import DestroyModelMixin
from rest_framework.serializers import Serializer
from app.models import Comment, CommentLike, Flower
from app.serializers import *
from app.permissions import (DeleteOnly, HasObjectPermission)

class CommentsViewSet(DestroyModelMixin, ViewSet):
    permission_classes = [DeleteOnly, HasObjectPermission]
    serializer_class = Serializer

    def get_object(self):
        obj = Comment.objects.get(id=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
