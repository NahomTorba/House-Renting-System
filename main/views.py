from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PropertyForm, Property
from django.contrib import messages  # Import messages to use Django's messages framework
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request): 
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        user_name = request.POST['user_name']
        user_email = request.POST['user_email']
        subject = request.POST['subject']
        message = request.POST['message']

        # send an e-mail
        send_mail(
            subject, # subject of the email
            message, #the message
            user_email, #from email
            ['nahom.torba@bitscollege.edu.et'], # to email
          )
        # pass user_name to the contact.html
        return render(request, 'contact.html', {'user_name': user_name})
    else:
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html')

def property_agent(request):
    return render(request, 'property-agent.html')

@login_required(login_url='login')
def property_list(request):
    properties = Property.objects.all()
    print("Properties: ", properties)
    return render(request, 'property-list.html', {'properties': properties})

@login_required(login_url='login')
def property_type(request):
    return render(request, 'property-type.html',)

def testimonial(request):
    return render(request, 'testimonial.html')

def not_found(request):
    return render(request, '404.html')

def set_language(request):
    return render(request, 'set_language.html')

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/index.html')
        else:
            messages.error(request, 'Username or Password is incorrect')
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already taken')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                return redirect('/Login.html')
        else:
            messages.error(request, 'Passwords do not match')

    return render(request, 'signup.html')

@login_required(login_url='login')
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.user = request.user
            property.save()
            print("Property saved successfully")
            return redirect('property-list')
        else:
            print("Form is not valid")
            print(form.errors)
            return render(request, 'add_property.html', {'form': form})
    else:
        form = PropertyForm()
        return render(request, 'add_property.html', {'form': form})