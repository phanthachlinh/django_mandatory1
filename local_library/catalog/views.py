from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Book,Magazine
from django.contrib.auth.models import User
from django.template import loader
from django.urls import reverse
import json,datetime
from django.db.models import Q
from datetime import timedelta

# Create your views here.
def index(request):

    if("error" in request.GET):
        print('error')
    return render(request,'catalog/login.html')

def register(request):

    return render(request,'catalog/register.html',{"post_url": "register/save"})

def saveuser(request):

    if(request.POST["password1"] != request.POST["password2"]):
        return render(request,'catalog/register.html',{"error":0,"post_url": "save"})

    new_user = User(username = request.POST["username"])
    new_user.set_password(request.POST["password1"])
    new_user.save()
    request.session['userId'] = new_user.id
    return redirect('/catalog/list')

def logout(request):

    del request.session['userId']
    return redirect('/catalog')

def signin(request):

    user = User.objects.get(username=request.POST['username'])

    if(not user.check_password(request.POST['password'])):
        return redirect('/catalog?error=true')
    else:
        print(user.id)
        request.session['userId'] = user.id
        return redirect('/catalog/list')


def list(request):

    if(not "userId" in request.session):
        return redirect('/catalog')

    print( User.objects.filter(id = request.session['userId']))

    context = {
        'available_books': Book.objects,
        'available_magazines': Magazine.objects,
        'user': User.objects.filter(id = request.session['userId'])[0],
        'max_checkout_limit_reached': False,
        'max_checkout_limit_reached_magazine': False
    }

    if(len(Book.objects.filter(user = User.objects.get(id = request.session['userId']))) >= 5):
        context['max_checkout_limit_reached'] = True

    if(len(Magazine.objects.filter(user = User.objects.get(id = request.session['userId']))) >= 3):
        context['max_checkout_limit_reached_magazine'] = True

    return render(request,'./catalog/index.html',context)


def checkout(request):

    context = {
        'available_books': Book.objects,
        'available_magazines': Magazine.objects,
        'max_checkout_limit_reached': False,
        'max_checkout_limit_reached_magazine': False
    }
    print(len(Book.objects.filter(user = User.objects.get(id = request.session['userId']))))

    if("bookId" in request.POST):
        Book.objects.filter(id = int(request.POST['bookId'])).update(checkout_date = datetime.datetime.now()+timedelta(days=30),user = User.objects.get(id = int(request.session['userId'])))

    if(len(Book.objects.filter(user = User.objects.get(id = request.session['userId']))) >= 5):
        context['max_checkout_limit_reached'] = True

    if(len(Magazine.objects.filter(user = User.objects.get(id = request.session['userId']))) >= 3):
        context['max_checkout_limit_reached_magazine'] = True

    return render(request,'catalog/index.html',context)

def checkout_magazine(request):

    context = {
        'available_books': Book.objects,
        'available_magazines': Magazine.objects,
        'max_checkout_limit_reached': False,
        'max_checkout_limit_reached_magazine': False
    }

    if("magazineId" in request.POST):
        Magazine.objects.filter(id = int(request.POST['magazineId'])).update(checkout_date = datetime.datetime.now()+timedelta(days=7),user = User.objects.get(id = int(request.session['userId'])))

    if(len(Book.objects.filter(user = User.objects.get(id = request.session['userId']))) >= 5):
        context['max_checkout_limit_reached'] = True

    if(len(Magazine.objects.filter(user = User.objects.get(id = request.session['userId']))) >= 3):
        context['max_checkout_limit_reached_magazine'] = True
    return render(request,'catalog/index.html',context)

def mypage(request):
    my_books = Book.objects.filter(user = User.objects.get(id = request.session['userId']))
    my_magazines = Magazine.objects.filter(user = User.objects.get(id = request.session['userId']))
    return render(request, 'catalog/mypage.html',{
    "my_books": my_books,
    "my_magazines": my_magazines,
    "user": User.objects.get(id=int(request.session['userId']))
    })

def checkin(request):

    if('bookId' in request.POST):
        Book.objects.filter(id= int(request.POST['bookId'])).update(user= None, checkout_date = None)
    if('magazineId' in request.POST):
        Magazine.objects.filter(id= int(request.POST['magazineId'])).update(user= None, checkout_date = None)
    return redirect('/catalog/mypage')

def manage(request):
    checkouted_books = Book.objects.filter(~Q(user = None),checkout_date__lte = datetime.datetime.now())
    checkouted_magazines = Magazine.objects.filter(~Q(user = None),checkout_date__lte = datetime.datetime.now())
    context = {
        "checkouted_books":checkouted_books,
        "checkouted_magazines":checkouted_magazines
    }
    return render(request,'catalog/manage.html',context)
