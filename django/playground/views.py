from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def say_hello(request):
    # DB
    # TRANSFORM
    # SEND MAIL
    return HttpResponse('Frits was here')

def withTemplate(request):
    # DB
    # TRANSFORM
    # SEND MAIL
    return render(request, 'index.html')

def withTemplateWithVariable(request):
    # DB
    # TRANSFORM
    # SEND MAIL
    return render(request, 'index.html', {
        'name': 'decreasenl'
    })