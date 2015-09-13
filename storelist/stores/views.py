# coding: utf-8
from .models import Store
from .serializer import StoreSerializer

from rest_framework.viewsets import ModelViewSet


class StoreViewSet(ModelViewSet):
    queryset = Store.objects.order_by('id')
    serializer_class = StoreSerializer
