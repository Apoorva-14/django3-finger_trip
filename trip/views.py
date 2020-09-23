from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import TripForm, CommentForm
from .models import Trip, Like, Comment, Contact
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

#Home
def home(request):
    return render(request, 'trip/home.html')

#About
def about(request):
    return render(request, 'trip/about.html')

#Contact
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name)<2 or len(email)<10 or len(phone)<10 or len(content)<4:
            messages.error(request, 'Please fill the form correctly ⚠️')
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, 'Your message has been successfully sent 📨')
    return render(request, 'trip/contact.html')

#Wall
@login_required
def wall(request):
    trips = Trip.objects.order_by('-updated')
    liker = request.user

    context = {
        'trips' : trips,
        'liker' : liker
    }

    return render(request, 'trip/wall.html', context)


@login_required
def like_post(request):
    liker = request.user
    if request.method == 'POST':
        trip_id = request.POST.get('trip_id')
        trip_obj = Trip.objects.get(id=trip_id)

        if liker in trip_obj.likes.all():
            trip_obj.likes.remove(liker)
        else:
            trip_obj.likes.add(liker)

        like, created = Like.objects.get_or_create(liker=liker, trip_id=trip_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()
    return redirect('wall')


@login_required
def trip_detail(request,trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    if request.method == "GET":
        return render(request, 'trip/trip_detail.html', {'form':CommentForm(),'trip':trip})
    else:
        try:
            form = CommentForm(request.POST)
            newcomment = form.save(commit=False)
            newcomment.user = request.user
            newcomment.save()

            return redirect('wall')
        except IntegrityError:
            return render(request, 'trip/trip_detail.html', {'form':CommentForm(), 'error':'Bad data passed in, Try again','trip':trip})


@login_required
def comment_post(request):
    return redirect('wall')


#Authentication
def signupuser(request):
    if request.method == "GET":
        return render(request, 'trip/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentuploads')
            except IntegrityError:
                return render(request, 'trip/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken'})
        else:
            return render(request, 'trip/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})


def loginuser(request):
    if request.method == "GET":
        return render(request, 'trip/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'trip/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('currentuploads')


@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')


#Uploading
@login_required
def createuploads(request):
    if request.method == "GET":
        return render(request, 'trip/createuploads.html', {'form':TripForm()})
    else:
        try:
            form = TripForm(request.POST)
            newpost = form.save(commit=False)
            newpost.user = request.user
            newpost.save()
            return redirect('currentuploads')
        except ValueError:
            return render(request, 'trip/createuploads.html', {'form':TripForm(), 'error':'Bad data passed in, Try again'})


@login_required
def currentuploads(request):
    trips = Trip.objects.filter(user=request.user)
    return render(request, 'trip/currentuploads.html', {'trips':trips})


@login_required
def viewtrip(request, trip_pk):
    trip = get_object_or_404(Trip, pk=trip_pk, user=request.user)
    if request.method == "GET":
        form = TripForm(instance=trip)
        return render(request, 'trip/viewtrip.html', {'trip':trip,'form':form})
    else:
        try:
            form = TripForm(request.POST, instance=trip)
            form.save()
            return redirect('currentuploads')
        except ValueError:
            return render(request, 'trip/viewtrip.html', {'trip':trip,'form':form, 'error':'Bad Info'})


@login_required
def deletetrip(request, trip_pk):
    trip = get_object_or_404(Trip, pk=trip_pk, user=request.user)
    if request.method == "POST":
        trip.delete()
        return redirect('currentuploads')
