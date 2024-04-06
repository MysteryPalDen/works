from django.urls import path

from .views import *

urlpatterns = [
    path('', page_main, name='home'),
    path('recieve', page_recieve, name='recieve')
]