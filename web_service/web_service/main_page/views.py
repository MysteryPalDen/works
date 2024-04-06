from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Recieve

# Create your views here.
menu = ['A', 'B', 'C']
def page_main(request):
    obj = Recieve.objects.all()
    return render(request, 'main_page/mainest.html', {'menu': menu, 'obj': obj})

def page_recieve(request, id):
    return HttpResponse(f"<h1>Cтраница</h1><p>{id}</p>")