from django.db import router
from django.urls import path
from rest_framework_nested import routers

from . import views


router = routers.DefaultRouter()
router.register('bets', views.BetCodeViewSet)
router.register('posts', views.PostViewSet, basename='comments')
router.register('profileposts', views.ProfilePostViewSet,
                basename='profile-comments')
router.register('clubs', views.FootballClubViewSet)
router.register('bookcodeinfo', views.BookCodeInfoViewSet)

posts_router = routers.NestedDefaultRouter(router, 'posts', lookup='post')
posts_router.register('comments', views.CommentViewSet,
                      basename='post-comments')
posts_router.register('likes', views.LikesViewSet, basename='post-likes')

comments_router = routers.NestedDefaultRouter(
    posts_router, 'comments', lookup='comment')
comments_router.register('replys', views.ReplyViewSet,
                         basename='comment-replys')
# comments_router.register('likes', views.LikesViewSet, basename='post-likes')


# URLConf
urlpatterns = router.urls + posts_router.urls


# urlpatterns = router.urls + products_router.urls + carts_router.urls
