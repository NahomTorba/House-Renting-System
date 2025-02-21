from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import PropertyForm, Property, SignUpForm, Request, UserMessage, UserMessageForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request): 
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create and save UserMessage instance
        user_message = UserMessage(
            name=user_name,
            email=user_email,
            message=message,
        )
        user_message.save()

        return render(request, 'contact.html', {'user_name': user_name})

    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def property_agent(request):
    return render(request, 'property-agent.html')

@login_required(login_url='login')
def property_list(request):
    properties = Property.objects.filter(available='available')  # Filter to only available properties
    
    # Get filter values from the request
    property_type = request.GET.get('property_type', '').strip()
    property_for = request.GET.get('property_for', '').strip()
    location = request.GET.get('location', '').strip()
    price_min = request.GET.get('price_min', '').strip()
    price_max = request.GET.get('price_max', '').strip()

    # Applying the filters for property_type
    if property_type and property_type in dict(Property.PROPERTY_TYPES):
        properties = properties.filter(property_type=property_type)

    # Applying the filters for property_for
    if property_for and property_for in dict(Property.PROPERTY_FOR):
        properties = properties.filter(property_for=property_for)

    # Applying the filters for location
    if location:
        properties = properties.filter(location__icontains=location)

    # Applying the filters for price range
    if price_min.isdigit():
        properties = properties.filter(price__gte=int(price_min))
    if price_max.isdigit():
        properties = properties.filter(price__lte=int(price_max))
    
    no_results = not properties.exists()

    return render(request, 'property-list.html', {'properties': properties, 'no_results': no_results})

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
            return redirect('/index')
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
                return redirect('login')
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

@login_required(login_url='login')
def edit_property(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id, user=request.user)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property_obj)
        if form.is_valid():
            form.save()
            return redirect('property-list')
        else:
            print(form.errors)  # Print errors to the console for debugging
    else:
        form = PropertyForm(instance=property_obj)
    
    return render(request, 'edit_property.html', {'form': form, 'property': property_obj})

@login_required(login_url='login')
def delete_property(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id, user=request.user)
    if request.method == 'POST':
        property_obj.delete()
        return redirect('property-list')

    return render(request, 'delete_property.html', {'property': property_obj})

def chapa(request):
    return render(request, 'chapa.html')


@login_required(login_url='login')
def view_requests(request, property_id):
    # Fetch the property object, ensuring that the logged-in user is the owner
    property_obj = get_object_or_404(Property, id=property_id, user=request.user)
    
    # Fetch all requests associated with that property
    requests = Request.objects.filter(property=property_obj)

    return render(request, 'view_requests.html', {'property': property_obj, 'requests': requests})

@login_required(login_url='login')
def update_requests(request, request_id):
    request_instance = get_object_or_404(Request, id=request_id)
    
    # Ensure that the logged-in user is the owner of the property associated with the request
    if request_instance.property.user != request.user:
        messages.error(request, 'You are not authorized to update this request.')
        return redirect('property-list')

    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['accepted', 'rejected']:
            request_instance.status = status
            request_instance.save()
            messages.success(request, f'Request status updated to {status.capitalize()}!')
        else:
            messages.error(request, 'Invalid status update.')

        return redirect('view_requests', property_id=request_instance.property.id)

    return render(request, 'update_requests.html', {'request': request_instance})

@login_required(login_url='login')
def delete_request(request, request_id):
    request_instance = get_object_or_404(Request, id=request_id)

    # Ensure that the request sender is the one trying to delete the request
    if request_instance.user != request.user:
        messages.error(request, 'You are not authorized to delete this request.')
        return redirect('property-list')

    if request.method == 'POST':
        request_instance.delete()
        messages.success(request, 'Request deleted successfully!')
        return redirect('user_requests')  # Redirect to user's requests

    return render(request, 'delete_request.html', {'request': request_instance})

@login_required(login_url='login')
def user_requests(request):
    # Fetch all requests made by the logged-in user
    user_requests = Request.objects.filter(user=request.user)

    return render(request, 'user_requests.html', {'requests': user_requests})

@login_required(login_url='login')
def send_request(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)

    if request.method == 'POST':
        description = request.POST.get('description')
        price = request.POST.get('price')

        # Create a new request
        new_request = Request.objects.create(
            user=request.user,
            property=property_obj,
            description=description,
            price=price,
            status='pending'  # Default status
        )
        messages.success(request, 'Request sent successfully!')
        return redirect('user_requests')

    return render(request, 'send_request.html', {'property': property_obj})