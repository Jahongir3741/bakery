from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
            DiroctorViewSet, 
            VendorViewSet, 
            BakerViewSet, 
            ClientViewSet, 
            RegisterAPIView,
            UserChangePasswordAPIView
    )

router = DefaultRouter()
router.register('director', DiroctorViewSet, basename='director')
router.register('vendor', VendorViewSet, basename='vendor')
router.register('baker', BakerViewSet, basename='baker')
router.register('client', ClientViewSet, basename='client')

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('users/change-password/',UserChangePasswordAPIView.as_view(), name='change_password'),
    path('', include(router.urls))
]

