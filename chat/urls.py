from django.urls import path
from django.urls.resolvers import URLPattern
from django.views.generic.base import View
from .views import ChatView, RoomView

urlpatterns = [ 
    path('', ChatView.as_view(), name='index'),
    path('<str:room_name>/', RoomView.as_view(), name='room')
]