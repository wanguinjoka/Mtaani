from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import DetailView, CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Kijiji
# Create your views here.
def home(request):
    context={
        'kijijis': Kijiji.objects.all()
    }
    return render(request,'neighbourhood/home.html', context)

class KijijiDetailView(LoginRequiredMixin, DetailView):
     model = Kijiji
