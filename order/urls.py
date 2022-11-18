from rest_framework.routers import SimpleRouter
from .views import OrderViewSet, OrderItemAPIView
from django.urls import path, include

router = SimpleRouter()
router.register('order', OrderViewSet, basename='order')
# router.register('orderitem', OrderItemViewSet, basename='orderitem')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:breadItem_id>/<int:order_id>/orderItem/', OrderItemAPIView.as_view()),
]
