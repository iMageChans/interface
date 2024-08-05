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
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="D9Server",
        default_version='v1',
        description="API documentation for D9Server",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

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
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
