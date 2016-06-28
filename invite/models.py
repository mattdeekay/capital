from django.db import models

from django.conf import settings
from django.contrib.auth.views import login
from django.http import HttpResponseRedirect

from social.backends.oauth import BaseOAuth2

class GithubOAuth2(BaseOAuth2):
    """Github OAuth authentication backend"""
    name = 'github'
    AUTHORIZATION_URL = 'https://github.com/login/oauth/authorize'
    ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'
    SCOPE_SEPARATOR = ','
    EXTRA_DATA = [
        ('id', 'id'),
        ('expires', 'expires')
    ]

    def get_user_details(self, response):
        """Return user details from Github account"""
        return {'username': response.get('login'),
                'email': response.get('email') or '',
                'first_name': response.get('name')}

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        url = 'https://api.github.com/user?' + urlencode({
            'access_token': access_token
        })
        try:
            return json.load(self.urlopen(url))
        except ValueError:
            return None

class PinterestOAuth2(BaseOAuth2):
    """Pinterest OAuth authentication backend"""
    name = 'pinterest'
    AUTHORIZATION_URL = 'https://api.pinterest.com/oauth/'
    ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'
    SCOPE_SEPARATOR = ','
    EXTRA_DATA = [
        ('id', 'id'),
        ('expires', 'expires')
    ]
    RESPONSE_TYPE = 'code'
    REDIRECT_STATE = 'https://www.google.com/'

    def get_user_details(self, response):
        """Return user details from Github account"""
        return {'username': response.get('login'),
                'email': response.get('email') or '',
                'first_name': response.get('name')}

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        url = 'https://api.github.com/user?' + urlencode({
            'access_token': access_token
        })
        try:
            return json.load(self.urlopen(url))
        except ValueError:
            return None

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
