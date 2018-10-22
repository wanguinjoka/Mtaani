from django.conf.urls import url
from .views import KijijiDetailView,NewsCreateView
from . import views

urlpatterns=[
    url('^$', views.home, name='home'),
    url(r'^kijiji/(?P<pk>[0-9]+)/$', KijijiDetailView.as_view(), name='kijiji-detail'),
    url(r'^Kijiji/news/', NewsCreateView.as_view(), name='news-create'),
]
