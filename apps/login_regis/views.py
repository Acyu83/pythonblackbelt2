from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages

def index(request):

    if id in request.session:
        request.session.clear()

    print User.objects.all()
    return render(request, 'login_regis/index.html')

def process(request):
    x = User.objects.register(request.POST)
    if x[0] == True:
        messages.success(request, "Registration Successful")
    else:
        for error in x[1]:
            messages.error(request, error)
    return redirect("/")

def login(request):
    y = User.objects.login(request.POST)

    if y[0] == True:
        request.session["id"] = y[2]
        return redirect("/success")
    else:
        for error in y[1]:
            messages.error(request, error)
        return redirect("/")

def success(request):
    this_user = User.objects.get(id=request.session["id"])


    context = {
        "names" : User.objects.get(id=request.session["id"]),
        "nonfriends": User.objects.exclude(friend_id=this_user),
        "friends": User.objects.filter(friend_id=this_user),
        "stranger": User.objects.exclude(id=this_user.id)
    }


    return render(request, "login_regis/success.html", context)

def add_process(request, id):
    this_user = User.objects.get(id=request.session["id"])
    friendee = User.objects.get(id=id)
    friend = friendee.friend_id.add(this_user)
    return redirect("/success")

def view_friend(request, id):
    friend = User.objects.get(id=id)
    context = {
        "friend" : User.objects.get(id=id)
    }

    return render(request, "login_regis/friend.html", context)

def delete_process(request, id):
    this_user = User.objects.get(id=request.session["id"])
    friend = User.objects.get(id=id)
    removing = friend.friend_id.remove(this_user)
    return redirect("/success")

def logout(request):
    return redirect("/")


def error(request):
    return redirect("/")
