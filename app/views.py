from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm
from .models import Room, Message

@login_required
def index(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, "chat/index.html",{'users':users})


@login_required
def room(request, room_name):
    room,_ = Room.objects.get_or_create(name = room_name)
    user = request.user

    if user not in room.users.all() : 
        room.users.add(user)

    msgs = Message.objects.filter( room = room ).order_by('date')

    return render(request, "chat/room.html", {"room_name": room_name,"messages":msgs,'room':room})



def login (request) : 
    return HttpResponse('Login')




def register (request) : 
    
    form = RegisterForm()

    if request.method == "POST" : 
        form = RegisterForm(request.POST)

        if form.is_valid() : 
            username = request.POST['username']
            email = request.POST['email']
            pas = request.POST['password']

            User.objects.create_user(
                username = username,
                email = email,
                password = pas,
            ).save()

            return redirect('login')

    return render(request,'auth/register.html',{'form':form})