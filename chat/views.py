from django.http import request
from django.shortcuts import render
from django.views import View

# Create your views here.


class ChatView(View):
    def get(self, request): 
        return render(request, template_name='chat/index.html')



class RoomView(View):
    def get(self, request, room_name):
        context = {
            'room_name': room_name
        }
        return render(request, template_name='chat/room.html', context=context)
