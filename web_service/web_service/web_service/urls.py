"""
URL configuration for web_service project.

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
from django.urls import path
from main_page.views import page_main, page_recieve
from main_page.views import BaseAPIView
from django.views.static import serve as mediaserve
from django.urls import include, re_path
from web_service import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_page/', page_main),
    path('', include('main_page.urls')),
    path('api/datalist', BaseAPIView.as_view(), name='api')
]

if not (settings.DEBUG):
    urlpatterns+= [
        re_path(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$', mediaserve, {'document_root': settings.STATIC_ROOT}),
    ]