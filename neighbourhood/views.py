from django.shortcuts import render
from django.http import HttpResponse
from .models import Kijiji
# Create your views here.
def home(request):
    context={
        'kijijis': Kijiji.objects.all()
    }
    return render(request,'neighbourhood/home.html', context)
