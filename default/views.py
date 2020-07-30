from django.shortcuts import render
from .models import *

# Create your views here.
def get_client_ip(request):
    ip = 123

    return ip

def defaults(request):
    prod =Prod.objects.all()
    exemps = Exemple.objects.all()[0:4]
    exemps1 = [exemps[0], exemps[2]]
    exemps2 = [exemps[1], exemps[3]]
    print(get_client_ip(request))
    return render(request,'index.html',{'prods':[prod[0],prod[1]],'exemps1':exemps1,'exemps2':exemps2})

def faq(request):
    print(get_client_ip(request))
    exemps= Exemple.objects.all()[0:4]
    exemps1 = [exemps[0],exemps[2]]
    exemps2 = [exemps[1], exemps[3]]
    return render(request,'faq.html',{'exemps1':exemps1,'exemps2':exemps2})

def comment(request):
    return render(request,'comm.html')