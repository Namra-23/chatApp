from django.shortcuts import render, redirect
from .models import ChatRoom, ChatMessage

# Create your views here.


def index(request):
    chatrooms = ChatRoom.objects.all()
    return render(request, 'chatapp/index.html', {'chatrooms': chatrooms})


def chatroom(request, slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=chatroom)[0:30]
    return render(request, 'chatapp/room.html', {'chatroom': chatroom,'messages':messages})

def aboutus(request):
    return 	render ( request,"chatapp/aboutus.html")
