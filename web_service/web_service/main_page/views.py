from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .forms import RegisterUserForm, LoginUserForm, AddController
#from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
import random
import string
from datetime import datetime, timedelta
from django.db import connection
#from .serializers import RecieveSerializer

def random_string(length):
    characters = string.ascii_letters + string.digits
    result = ''.join(random.choice(characters) for _ in range(length))
    return result

class BaseAPIView(APIView):
    def get(self, request):
        return Response({'name': 'lol','title': 2})
'''
def my_view(request):
    if request.method == 'POST':
        if 'my_button' in request.POST:
            new_record = Recieve(name='name', device=1111)
            new_record.save()
'''
'''
class BaseAPIView(generics.ListAPIView):
    queryset = Recieve.objects.all()
    serializer_class = RecieveSerializer
'''

# Create your views here.
menu = ['A', 'B', 'C']
dic = {}


def page_main(request):
    obj = Recieve.objects.all()
    return render(request, 'main_page/mainest.html', {'menu': menu, 'obj': obj})

def personal(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    one_entry = Users.objects.get(login = username)
    if request.method == 'POST':
        form = AddController(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            rnd_str = random_string(20)
            while Controllers.objects.filter(special_key=rnd_str).exists():
                rnd_str = random_string(20)
            Controllers.objects.create(controller_name=name, special_key=rnd_str)
            contr_entry = Controllers.objects.get(special_key=rnd_str)
            Controllers_Users.objects.create(user=one_entry, controller=contr_entry)
            return redirect('personal_area')
    else:
        form = AddController()
    data = Controllers_Users.objects.select_related('user', 'controller').filter(user_id = one_entry)

    data_2 = Recieve.objects.raw("SELECT * FROM main_page_recieve INNER JOIN main_page_emergencies ON main_page_recieve.emergency_id = main_page_emergencies.id \
JOIN main_page_controllers ON main_page_recieve.controller_id = main_page_controllers.id JOIN main_page_controllers_users \
ON main_page_controllers.id = main_page_controllers_users.controller_id JOIN main_page_users ON main_page_controllers_users.user_id = \
main_page_users.id WHERE main_page_users.login = %s AND emergency_id > 4", [username])
    data_3 = Recieve.objects.raw("SELECT * FROM main_page_recieve INNER JOIN main_page_emergencies ON main_page_recieve.emergency_id = main_page_emergencies.id  \
                                 JOIN main_page_controllers ON main_page_recieve.controller_id = main_page_controllers.id JOIN main_page_controllers_users ON main_page_controllers.id \
                                 = main_page_controllers_users.controller_id JOIN main_page_users ON main_page_controllers_users.user_id = main_page_users.id WHERE main_page_users.login = \
                                 %s AND main_page_recieve.emergency_id >= 1 AND main_page_recieve.emergency_id <= 4 AND main_page_recieve.time_right_now > DATE_SUB(CURRENT_DATE, INTERVAL 1 MONTH)", [username])
    water_amount = 0
    with connection.cursor() as cursor:
        cursor.execute("SELECT count(*) FROM main_page_recieve INNER JOIN main_page_emergencies ON main_page_recieve.emergency_id = main_page_emergencies.id  \
                        JOIN main_page_controllers ON main_page_recieve.controller_id = main_page_controllers.id JOIN main_page_controllers_users ON main_page_controllers.id \
                        = main_page_controllers_users.controller_id JOIN main_page_users ON main_page_controllers_users.user_id = main_page_users.id WHERE main_page_users.login = \
                        %s AND main_page_recieve.emergency_id >= 1 AND main_page_recieve.emergency_id <= 4 AND main_page_recieve.time_right_now > DATE_SUB(CURRENT_DATE, INTERVAL 1 MONTH)", [username])
        weter = cursor.fetchone()
        water_amount = weter[0] * 10
    dic.update({"data": data, "data_2": data_2, "data_3": data_3, "form": form, "water_amount": water_amount})
    return render(request, 'main_page/personal_area.html', dic)

def page_register(request):
    return render(request, 'main_page/register.html')

def page_login(request):
    return render(request, 'main_page/log_in.html')

"""
@api_view(['POST'])
def page_recieve(request):
    if request.method == 'GET':
        name_r = (request.POST.get('name', ''))
        device_r = int(request.POST.get('device', '2'))
        new_record = Recieve(name=name_r, device=device_r)
        new_record.save()
        data = {
            'message': 'POST request received',
            'data': name_r
        }
        return JsonResponse(data)
"""

@csrf_exempt
def page_recieve(request):
    if request.method == 'POST':
        data = {
            'message': 'POST request was not received',
            'data': "lol"
        }
        name_r = request.body.decode('utf-8')
        message = name_r.split(";")
        if message[0] == str(1):
            if Controllers.objects.filter(special_key=message[1]).exists():
                em_entry = Emergencies.objects.get(id=message[2])
                contr_entry = Controllers.objects.get(special_key=message[1])
                Recieve.objects.create(controller=contr_entry, emergency=em_entry, time_right_now=(datetime.now()+datetime.timedelta(hours=3)))
                data = {
                    'message': 'Data was saved',
                    'data': "lol"
                }
            else:
                data = {
                    'message': 'No such controller',
                    'data': "lol"
                }
        if message[0] == str(0):
            if Controllers.objects.filter(special_key=message[1]).exists():
                em_entry = Emergencies.objects.get(id=message[2])
                contr_entry = Controllers.objects.get(special_key=message[1])
                Recieve.objects.create(controller=contr_entry, emergency=em_entry, time_right_now=datetime.now())
                data = {
                    'message': 'Data was saved',
                    'data': "lol"
                }
            else:
                data = {
                    'message': 'No such controller',
                    'data': "lol"
                }
        return JsonResponse(data)

"""
@csrf_exempt
def page_recieve(request):
    if request.method == 'GET':
        name_r = (request.GET.get('name', ''))
        device_r = int(request.GET.get('device', ''))
        new_record = Recieve(name=name_r, device=device_r)
        new_record.save()
        data = {
            'message': 'POST request received',
            'data': name_r
        }
        return JsonResponse(data)
"""

def registration(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Users.objects.create(login=form.cleaned_data.get('username'), usrpswd = form.cleaned_data.get('password1'),first_name=form.cleaned_data.get('first_name'), last_name=form.cleaned_data.get('last_name'), login_str=form.cleaned_data.get('email'), phone=form.cleaned_data.get('phone'))
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form': form})

def log_in(request):
    if request.method == 'GET':
        form = LoginUserForm()
        return render(request, 'log_in.html', {'form': form})
    elif request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            raw_password = form.cleaned_data['password']
            user = authenticate(username=user_name, password=raw_password)
            if user:
                login(request, user)
                messages.success(request,f'Hello, {user_name.title()}')
                return redirect('/')
        messages.error(request, f'Invalid username or password')
        return render(request, 'log_in.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect('/')