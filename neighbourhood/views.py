from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import DetailView, CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateNewsForm
from .models import Kijiji, News
# Create your views here.
def home(request):
    context={
        'kijijis': Kijiji.objects.all()
    }
    return render(request,'neighbourhood/home.html', context)

class KijijiDetailView(LoginRequiredMixin, DetailView):
     model = Kijiji

# @login_required(login_url='/accounts/login/')
# def new_news(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = CreateNewsForm(request.POST, request.FILES)
#         if form.is_valid():
#             news = form.save(commit=False)
#             news.author = current_user
#             news.save()
#         return redirect('')
#
#     else:
#         form = CreateNewsForm()
#     return render(request, 'new_article.html', {"form": form})

class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    fields = ['tag','cation','kijiji']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
