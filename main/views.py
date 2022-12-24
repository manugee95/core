from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import CareerForm

# Create your views here.

def home(request):
    info = HomeProfile.objects.get(pk=1)
    serviceinfo = Service.objects.filter(servicess= True)

    context = {
        'info':info,
        'serviceinfo':serviceinfo
    }

    return render(request, 'index.html', context)

def service(request):
    maryland = Service.objects.filter(maryland=True)
    virginia = Service.objects.filter(virginia=True)
    columbia = Service.objects.filter(columbia=True)

    context = {
        'maryland':maryland,
        'virginia':virginia,
        'columbia':columbia,
    }

    return render(request, 'service.html', context)

def career(request):
    state = State.objects.all()
    stateapp = StateApplied.objects.all()
    positionapp = PositionApplied.objects.all()
    time = Time.objects.all()

    career = CareerForm()
    if request.method == 'POST':
        career = CareerForm(request.POST, request.FILES)
        if career.is_valid():
            career.save()
            messages.success(request, 'your form is submitted and now being reviewed, you will be contacted shortly')
            return redirect('home')
        else:
            messages.error(request, career.errors)
            return redirect('career')

    context = {
        'state':state,
        'stateapp':stateapp,
        'positionapp':positionapp,
        'time':time,
        'career':career,
    }

    return render(request, 'career.html', context)
