from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, FileResponse
from .models import Contacts
from django.conf import settings


# Create your views here.
def cv(request):
    return render(request, 'cv.html')


def Index(request):
    return render(request, 'index.html')


def Service(request):
    return render(request, 'services.html')


def Portfolio(request):
    return render(request, 'portfolio.html')


def Contact(request):
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact_message = Contacts.objects.create(name=name, email=email, message=message)
        contact_message.save()
    return render(request, 'contact.html')
