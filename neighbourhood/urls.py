from django.conf.urls import url
from .views import KijijiDetailView,NewsCreateView,BusinessCreateView, ProfileCreateView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$', views.home, name='home'),
    url(r'^kijiji/(?P<pk>[0-9]+)/$', KijijiDetailView.as_view(), name='kijiji-detail'),
    url(r'^news/new/', NewsCreateView.as_view(), name='news-create'),
    url(r'^business/new/', BusinessCreateView.as_view(), name='business-create'),
    url(r'^profile/new/', ProfileCreateView.as_view(), name='profile-create'),
    url(r'^profile/', views.profile, name = 'profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
