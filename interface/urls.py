"""
URL configuration for interface project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/amm/', include('amm.urls')),
    path('api/balances/', include('balances.urls')),
    path('api/users_profile/', include('users_profile.urls')),
    path('api/usdt/', include('usdt.urls')),
    path('api/main/mining/', include('main_mining.urls')),
    path('api/merchant/', include('merchant.urls')),
    path('api/qrcode/', include('qrcode.urls')),
    path('api/mining/', include('mining.urls')),
    path('api/votings/', include('votings.urls')),
    path('api/node/reward/', include('node_reward.urls')),
    path('api/referrals/', include('referrals.urls')),
    path('api/wallets/', include('wallets.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Redoc UI
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
