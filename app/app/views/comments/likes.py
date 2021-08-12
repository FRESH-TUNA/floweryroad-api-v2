from rest_framework.viewsets import ViewSet
from app.permissions import PostDeleteOnly
from app.mixins.comments.likes import (CreateModelMixin, DestroyModelMixin)
from app.models import CommentLike, Comment
from app.serializers import PurposeSerializer

class CommentsLikesViewSet(
    CreateModelMixin,
    DestroyModelMixin,
    ViewSet
):
    permission_classes = [PostDeleteOnly]

    # generic_viewset 에서는 기본값으로 지원하지만 router와의 연계를 위해 사용
    lookup_field = 'comment_pk'

    def get_object(self):
        return CommentLike.objects.get(
                user=self.request.user, comment=Comment.objects.get(id=self.kwargs["comment_pk"]))
