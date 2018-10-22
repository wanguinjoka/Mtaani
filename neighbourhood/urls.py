from django.conf.urls import url
from .views import KijijiDetailView,NewsCreateView,BusinessCreateView
from . import views

urlpatterns=[
    url('^$', views.home, name='home'),
    url(r'^kijiji/(?P<pk>[0-9]+)/$', KijijiDetailView.as_view(), name='kijiji-detail'),
    url(r'^news/new/', NewsCreateView.as_view(), name='news-create'),
    url(r'^business/new/', BusinessCreateView.as_view(), name='business-create'),
]
