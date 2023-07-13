from django.contrib import admin
from django.urls import path,include
from .import views
from .views import aboutus

urlpatterns = [
    path('',views.index,name='index'),
    path('about',aboutus,name='About'),
    path('<slug:slug>/',views.chatroom,name='chatroom'),
]