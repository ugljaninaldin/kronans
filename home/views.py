from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/index.html', {})

def team(request):
    return render(request, 'home/team.html', {})

def contact(request):
    return render(request, 'home/contact.html', {})
