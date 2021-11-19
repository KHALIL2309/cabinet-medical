from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import *

def client(request):
    return render (request , 'cabinetMedical/client.html')

def about(request):
    return HttpResponse('heee about')

def user(request):
    return HttpResponse('heee user')
    
def page(request):
    return render (request , 'cabinetMedical/projeet.html')  

def home(request):
    vclient = Client.objects.all()
    t_age = vclient.filter(age='20').count
    vorder = Order.objects.all()
    t_orders = vorder.count()
    a_orders = vorder.filter(status='arrived').count()
    l_orders = vorder.filter(status='lost').count()
    d_orders = vorder.filter(status='did_not_arrive').count()
    context = {'vclients' : vclient,
                't_age' : t_age ,
                'order': vorder ,
                't_orders' : t_orders,
                'a_orders' : a_orders,
                'l_orders' : l_orders,
                'd_orders' : d_orders }

    return render (request , 'cabinetMedical/home.html',context)   

def boook(request):
    vbook = book.objects.all()
    return render (request , 'cabinetMedical/book.html',{'Book': vbook})   

def projet3(request):
    return render (request , 'cabinetMedical/projet3.html')






# http://127.0.0.1:8000/