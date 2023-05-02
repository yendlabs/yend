from django.shortcuts import render,redirect,HttpResponse
from .models import Contact
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    dis = Contact.objects.all()

    if request.method == "POST":
        name2 = request.POST.get('name')
        email2 = request.POST.get('email')
        text2 = request.POST.get('message')
        doc = Contact.objects.create(name=name2, email=email2, text=text2)
        doc.save()
        
        return redirect('contact')

    return render(request, 'contact.html', {'dis':dis} )

