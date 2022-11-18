from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='obtainpair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('accounts.urls')),
    path('api/v1/', include('bakery.urls')),
    path('api/v1/', include('category.urls')),
    path('api/v1/', include('order.urls')),
]
