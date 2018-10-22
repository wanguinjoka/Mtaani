from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileUpdateForm
from django.contrib import messages
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

@login_required
def profile(request):
    if request.method == 'POST':

        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
                                   #request.FILES, instance=request.user.profile)

        if  p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:

        p_form = ProfileUpdateForm(instance=request.user.profile)


        context = { 'p_form':p_form}
        return render(request,'neighbourhood/profile.html', context)
