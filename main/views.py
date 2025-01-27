from django.shortcuts import render
from django.http import HttpResponse 
from django.core.mail import send_mail

# Create your views here.

# web pages below here.
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

def property_list(request):
    return render(request, 'property-list.html')

def property_type(request):
    return render(request, 'property-type.html')

def testimonial(request):
    return render(request, 'testimonial.html')




