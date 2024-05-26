from rest_framework import routers              # type: ignore

from django.contrib import admin                # type: ignore
from django.urls import include, path           # type: ignore

from cats.views import AchievementViewSet, CatViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'cats', CatViewSet, 'cats')
router.register(r'users', UserViewSet)
router.register(r'achievements', AchievementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
