from rest_framework.routers import SimpleRouter
from app.views import CommentsViewSet

comments_router = SimpleRouter(trailing_slash=False)
comments_router.register(r'comments', CommentsViewSet, basename='comments')
