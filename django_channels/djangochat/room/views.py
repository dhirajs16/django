from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Room

# Create your views here.
@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})


@login_required
def room(request, slug):
    room = get_object_or_404(Room, slug= slug)
    return render(request, 'room/room.html', {'room': room})