from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'home/index.html', {})

def team(request):
    return render(request, 'home/team.html', {})

def contact(request):
    if request.method == 'POST':
        email = request.POST['form_mail']
        subject = request.POST['subject']
        message = f"Email: {email}\nSubject: {subject}\nMessage: {request.POST['message']}"
        send_mail('Contact Form', message, 'settings.EMAIL_HOST_USER', ['aldinugljaninn@gmail.com'], fail_silently=False)
    return render(request, 'home/contact.html', {})
