from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CommentViewSet,
                       GroupViewSet, PostViewSet,
                       FollowViewSet,)

router_version1 = DefaultRouter()
router_version1.register('posts', PostViewSet, basename='posts')
router_version1.register('groups', GroupViewSet, basename='groups')
router_version1.register(
    'posts/(?P<post_id>\\d+)/comments',
    CommentViewSet,
    basename='comment')
router_version1.register('follow', FollowViewSet, basename='followers')

urlpatterns = [
    path('v1/', include(router_version1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
