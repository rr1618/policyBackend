"""policybackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from mediassist import views
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'customer', views.CustomerViewSet,basename='mediAssist')
#
# urlpatterns = [
#     path('medi/', include('mediAssist.urls')),
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('medi/', include('mediassist.urls')),
    path('rest/',include('mediassist.urls')),

]