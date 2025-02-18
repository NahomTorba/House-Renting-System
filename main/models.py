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
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=122)
    description = models.TextField()
    image = models.ImageField(upload_to='property_images' , default='\static\website\img\logo.jpg')
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    area = models.IntegerField(default=0)
    location = models.CharField(max_length=122)
    #latitude = models.FloatField(default=0)
    #longitude = models.FloatField(default=0)

    def __str__(self):
        return self.title


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'image', 'bedrooms', 'bathrooms', 'price', 'area', 'location']


    