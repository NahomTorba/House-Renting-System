from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()

    def __str__(self):
        return self.name

class Property(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=122)
    price = models.IntegerField()
    location = models.CharField(max_length=122)
    desc = models.TextField()
    photo = models.ImageField(upload_to='images')
    available_from = models.DateTimeField()
    available_to = models.DateTimeField()
    agent_name = models.CharField(max_length=122)
    agent_phone = models.CharField(max_length=12)
    agent_email = models.CharField(max_length=122)

    def __str__(self):
        return self.title

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user.username

    