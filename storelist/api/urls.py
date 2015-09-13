# coding:utf-8
from django.conf.urls import url
from stores.views import StoreViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stores', StoreViewSet)

helper_patterns = [
]

urlpatterns = helper_patterns
urlpatterns.extend(router.urls)
