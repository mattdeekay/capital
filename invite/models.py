from django.db import models

from django.conf import settings
from django.contrib.auth.views import login
from django.http import HttpResponseRedirect

class EmailAccess(models.Model):
    access_code = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email

class AccessCode(models.Model):
    access_code = models.CharField(max_length=100)

class UserRegister(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
'''
class RequireLoginMiddleware(object):
    def __init__(self):
        self.require_login_path=getattr(settings, 'REQUIRE_LOGIN_PATH', '/access/')
    def process_request(self, request):
        if request.path != self.require_login_path and request.user.is_anonymous():
            if request.POST:
                return login(request)
            else:
                return HttpResponseRedirect('%s?next=%s' % (self.require_login_path, request.path))
'''
