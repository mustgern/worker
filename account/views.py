from .forms import UserForm
from django.shortcuts import render, get_object_or_404 ,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from  .models import Users
import random
import string
import json
import requests
def randomString(stringLength):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))



def register(request):

    form = UserForm(request.POST)
    if request.method == "POST":
        post = Users()
        if (Users.objects.filter(login=form['login'].data)):
            return render(request, 'register.html', {'stat_reg': 'пользователь с таким именем сущствует'})
        if form.is_valid():
            post = form.save(commit=False)
            if (len(post.password) < 6):

                post.login = form['login'].data
                post.password = form['password'].data
                post.save()

                post.save()
                request.session['login']=post.login
            return render(request, 'register.html', {'form': form})



    return render(request, 'register.html', {'form': form})


def auth(request):
    form = UserForm(request.POST)
    if request.method == "POST":
            user = Users.objects.get(login = form['login'].data)
            if user.password==form['password'].data:
                    try:
                        del request.session['login']
                        request.session['login'] = form['login'].data
                    except:
                        request.session['login'] = form['login'].data
                    return render(request, 'auth.html', {'form': form})

            else:
                err = 'неверный пароль'
                return render(request, 'auth.html', {'form': form, 'err':err})

    return render(request, 'auth.html')

def change_mail(request):
    if request.method =="POST":

        old_u = Users.objects.get(login=request.session['login'])
        if request.POST['password']==old_u.password:
                old_u.email= request.POST['email']
                old_u.save()
                return render(request,'change_mail.html',{'form':old_u})
    return render(request, 'change_mail.html')

def change_pass(request):
    old_u = Users.objects.get(login=request.session['login'])
    if request.method == "POST":
        old_u = Users.objects.get(login=request.session['login'])
        new_pass = randomString(10)
        old_u.password = new_pass
        old_u.save()
        email_from = settings.EMAIL_HOST_USER
        subject ='Изменение пароля'
        message = 'Новый пароль:'+new_pass
        to_mail = [old_u.email]
        send_mail(subject, message, email_from,to_mail)
        del request.session['login']
        return render (request,'change_pass.html',{'user':old_u})
    return render(request, 'change_pass.html')