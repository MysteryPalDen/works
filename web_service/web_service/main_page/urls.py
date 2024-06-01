from django.urls import path



from .views import *

urlpatterns = [
    path('', page_main, name='home'),
    path('personal_area/', personal, name='personal_area'),
    path('recieve/', page_recieve, name='recieve'),
    path('register/', registration, name='register'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout')
]