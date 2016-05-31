from django import forms

from .models import EmailAccess, UserRegister
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class InterestForm(forms.ModelForm):

    class Meta:
        model = EmailAccess
        fields = ('email', 'access_code',)

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    #ndacheck = forms.BooleanField( initial=True, label="Agree to NDA")
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

