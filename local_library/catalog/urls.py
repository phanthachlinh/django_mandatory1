from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('register/save', views.saveuser),
    path('logout', views.logout),
    path('signin', views.signin),
    path('list', views.list),
    path('checkout', views.checkout),
    path('checkout_magazine', views.checkout_magazine),
    path('mypage', views.mypage),
    path('checkin', views.checkin),
    path('manage', views.manage)

]
