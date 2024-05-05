from django.shortcuts import render
from .models import Service, ContactMessage

def index(request):
    return render(request, 'index.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, message=message)
        return render(request, 'contact_success.html')
    return render(request, 'contact.html')
