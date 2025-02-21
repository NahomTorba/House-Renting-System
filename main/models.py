from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


# Create your models here.
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __str__(self):
        return self.username


class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=122)
    description = models.TextField()
    PROPERTY_TYPES = [('villa', 'Villa'), ('apartment', 'Apartment'), ('office', 'Office')]
    PROPERTY_FOR = [('sale', 'Sale'), ('rent', 'Rent')]
    AVAILABILITY_CHOICES = [
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('unavailable', 'Unavailable'),
        ('sold', 'Sold')
    ]
    
    property_type = models.CharField(max_length=122, choices=PROPERTY_TYPES, default='villa')
    property_for = models.CharField(max_length=122, choices=PROPERTY_FOR, default='sale')
    available = models.CharField(max_length=122, choices=AVAILABILITY_CHOICES, default='available')
    image = models.ImageField(upload_to='property_images', default='static/website/img/logo.jpg')
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    area = models.IntegerField(default=0)
    location = models.CharField(max_length=122)

    def __str__(self):
        return self.title


class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    PROPERTY_FOR = [('sale', 'Sale'), ('rent', 'Rent')]
    property_for = models.CharField(max_length=10, choices=PROPERTY_FOR, default='sale')
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Request by {self.user.username} for {self.property.title} - Status: {self.status}"


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'property_type', 'property_for', 'available', 'image', 'bedrooms', 'bathrooms', 'price', 'area', 'location']


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['property', 'price', 'description', 'property_for']


class UserMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.name} - {self.email}'

class UserMessageForm(forms.ModelForm):
    class Meta:
        model = UserMessage
        fields = ['name', 'email', 'message']