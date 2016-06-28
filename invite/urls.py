from django.conf.urls import url, include
from . import views

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from django.conf import settings
from django.conf.urls.static import static



#from two_factor.urls import urlpatterns as tf_twilio_urls

from django.contrib.auth.views import login as lgin

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    #url(r'', include('two_factor.urls', 'two_factor')),
    #url(r'', include(tf_urls + tf_twilio_urls, 'two_factor')),
    url(r'^access', views.access, name='access'),
    url(r'^login', lgin, {'template_name':'invite/login.html'}, name='login',),
    url(r'accounts/profile/$', views.lastpage, name='lastpage'),
    url(r'^register/$', views.register_user, name='register'),
    url(r'^lastpage/', views.lastpage, name='lastpagewoo'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^nda', views.nda, name='nda'), 
    url(r'^auth', views.auth, name='auth'),
    url(r'^social', include('social.apps.django_app.urls', namespace = 'social')),
    url(r'', include('django.contrib.auth.urls', namespace='auth')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
