
import code
from glob import glob
from lib2to3.pgen2.token import NAME
import random
from django import http
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail




def home(request):
    
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        code=random.randint(100000,990000)
        global global_code
        global_code=code
        print(name,email,code)

        send_mail(
        name,
        f'Your verification code is : {code}',
        'bilalzafar7474@gmail.com',
        [email],
        fail_silently=False,
        )
        return redirect("/")    
  
  
    return render(request,'index.html')




print(global_code)

