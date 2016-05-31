from django.conf.urls import url
from . import views

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^access', views.access, name='access'),
    url(r'^login', 'django.contrib.auth.views.login', {'template_name':'invite/login.html'}),
    url(r'accounts/profile/$', views.lastpage, name='lastpage'),
    url(r'^register/$', views.register_user, name='register'),
    url(r'^lastpage/', views.lastpage, name='lastpagewoo'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^nda', views.nda, name='nda'), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
