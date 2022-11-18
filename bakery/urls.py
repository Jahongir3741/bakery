from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BakeryViewSet, BreadViewSet, BreadItemViewSet

router = DefaultRouter()
router.register('bakery', BakeryViewSet, basename='bakeries')
router.register(r'^(?P<category_id>\d+)/bread', BreadViewSet, basename='breads')
router.register(r'^(?P<category_id>\d+)/(?P<bread_id>\d+)/breaditem', BreadItemViewSet, basename='breaditems')

urlpatterns = [
    path('', include(router.urls)),
]

