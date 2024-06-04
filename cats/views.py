from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets      # type: ignore
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.throttling import ScopedRateThrottle

from cats.models import Achievement, Cat, User
from cats.pagination import CatsPagination
from cats.permissions import OwnerOrReadOnly  # , ReadOnly
from cats.serializers import (
    AchievementSerializer, CatSerializer, UserSerializer)
from cats.throttling import WorkingHoursRateThrottle


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (OwnerOrReadOnly,)
    # throttle_classes = (WorkingHoursRateThrottle, ScopedRateThrottle)
    # throttle_scope = 'low_request'
    # pagination_class = CatsPagination
    # filter_backends = (DjangoFilterBackend, filters.SearchFilter,
    #                    filters.OrderingFilter)
    # filterset_fields = ('color', 'birth_year')
    # search_fields = ('name', 'achievements__name', 'owner__username')
    # ordering_fields = ('name', 'birth_year')
    # ordering = ('birth_year',)

    # # Пример выбора permissions в зависимости от условий
    # def get_permissions(self):
    #     # Если в GET-запросе требуется получить информацию об объекте
    #     if self.action == 'retrieve':
    #         # Вернём обновлённый перечень используемых пермишенов
    #         return (ReadOnly(),)
    #     # Для остальных ситуаций оставим текущий перечень пермишенов без изменений
    #     return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):                                   # Фильтрация 1 или 2
        queryset = Cat.objects.all()
        # print(self)
        # color = self.kwargs['color']                              # 1 НЕ РАБОТАЕТ БЕЗ нужных URLS, см. оф. доку, см. urls.py
        color = self.request.query_params.get('color')              # 2
        if color is not None:                                       # 2
            #  через ORM отфильтровать объекты модели Cat           # 2
            #  по значению параметра color, полученного в запросе   # 2
            queryset = queryset.filter(color=color)                 # 2
        # print(color)
        # Через ORM отфильтровать объекты модели Cat
        # по значению параметра color, полученного в запросе
        queryset = queryset.filter(color=color)
        return queryset


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
