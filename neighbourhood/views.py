from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import DetailView, CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Kijiji, News ,Business, Profile
# Create your views here.
def home(request):
    context={
        'kijijis': Kijiji.objects.all()
    }
    return render(request,'neighbourhood/home.html', context)

class KijijiDetailView(LoginRequiredMixin, DetailView):
     model = Kijiji


class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['image','bio','kijiji']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    fields = ['tag','cation','kijiji']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BusinessCreateView(LoginRequiredMixin, CreateView):
    model = Business
    fields = ['name','details','kijiji','contacts']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
