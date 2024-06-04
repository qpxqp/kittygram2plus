from rest_framework import routers              # type: ignore

from django.contrib import admin                # type: ignore
from django.urls import include, path, re_path           # type: ignore

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
    # path('api/cats/<str:color>/', CatViewSet.as_view({'get': 'list'}),  # 1 (вар.1) см. views.py
    #      name='cat-list'),
    # re_path('^api/cats/(?P<color>.+)/$', CatViewSet.as_view({'get': 'list'}),  # 1 (вар.2) см. views.py
    #         name='cat-list'),
]
