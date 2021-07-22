from app.views.base import BaseGenericViewSet
from app.permissions import CreateReadOnly
from app.serializers.flowers.comments import *
from app.paginators import *
from app.models import Comment, Flower
from app.mixins.flowers.comments import CreateModelMixin
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

class FlowersCommentsViewSet(CreateModelMixin, BaseGenericViewSet):
    pagination_class = FlowersCommentsPaginator
    permission_classes = [CreateReadOnly]

    def get_queryset(self):
        flower = Flower.objects.get(pk=self.kwargs['flower_pk'])
        return Comment.objects.select_related('user', 'flower').prefetch_related('comment_likes', 'flower__images').filter(flower_id=self.kwargs['flower_pk']).order_by('-created_at')
    
    def get_serializer_class(self):
        return FlowersCommentsSerializer
