from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import InterestForm, UserCreateForm, AccessForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import AccessCode

from django.http import HttpResponseRedirect

from datetime import datetime

from django.contrib.auth.forms import UserCreationForm

#from lockdown.decorators import lockdown

from django.contrib.auth.decorators import login_required, user_passes_test

#from django_otp.decorators import otp_required

def not_in_guest_group(user):
    if user:
        return user.groups.filter(name='Guest').count() == 0
    return False

def get_name(request):
    name = str(request.user)
    if name == "AnonymousUser":
        name = 'San Francisco'  #support for python2
    if name is "AnonymousUser":
        name = 'San Francisco'  #support for python3
    return name

#@login_required
def welcome(request):
    name = get_name(request)
    return render(request, 'invite/index.html', {'name': name})

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render(request, 'invite/index.html', {})
        else:
            return render(request, 'invite/disabled.html', {})
    else:
        return render(request, 'invite/invalid.html', {})
#@otp_required
def access(request):
    name = get_name(request)
    if request.method == "POST":
        form = InterestForm(request.POST)
        if form.is_valid():
            interest = form.save(commit=False)
            #print (interest.access_code == 'paloalto')
            #return redirect('nda')
            if AccessCode.objects.filter(access_code=interest.access_code).exists():
            #if (interest.access_code == 'paloalto'):
                #username = interest.username
                email = interest.email
                #print(email)
                #print(username)
                #user = authenticate(username=username)
                #if user is not None:
                #print(email)
                #print(interest.access_code)
                if User.objects.filter(email=email).exists():
                    #return render(request, 'invite/login.html', {'email':email})
                    return redirect('/login')
                else:
                    temp_username = 'temporary'
                    temp_password = 'djangotest'
                    user = authenticate(username=temp_username, password=temp_password)
                    if user is not None:
                        #print("User is valid")
                        login(request, user)
                    
                        #print("can't find you")
                    return redirect('register')
                    #return redirect('/register')
                    #return render(request, 'invite/newuser.html', {})
            else:
                return render(request, 'invite/invalid.html', {'name': name})
            
    else:
        form = InterestForm()
    return render(request, 'invite/access.html', {'form': form, 'name': name})


#@login_required(login_url='/access')
def nda(request):
    #print(email)
    name = get_name(request)
    if (request.GET.get('successbutton')):
        return render(request, 'invite/lastpage.html', {})
    return render(request, 'invite/nda.html', {'time':datetime.now().date(), 'name': name})

@login_required(login_url='/access')
@user_passes_test(not_in_guest_group, login_url='/access')
def lastpage(request):
    name = get_name(request)
    return render(request, 'invite/lastpage.html', {'name': name})

#@login_required(login_url='/access')
def logout_view(request):
    logout(request)
    return redirect('welcome')

#@lockdown(form=AccessForm)
#@login_required(login_url='/access')
@login_required(login_url='/access')
def register_user(request):
    name = get_name(request)
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        #print(form)
        if form.is_valid():
            #print("form is valid")
            #print(request.POST['ndacheck'])
            #ndacheck = NdaCheckBox(request.POST)
            #if request.POST['ndacheck']:
            #if request.POST['ndacheck'] is True:
            #check_values = request.POST.getlist('checks')
            #print (check_values)
            user = form.save(commit=False)
            username = user.username
            if User.objects.filter(username=username).exists():
                #print(username)
                form = UserCreateForm()
                return render(request, 'invite/register.html', {'userform':form, 'date':datetime.now().date(), 'message':"username already taken!", 'name': name})
            password = user.password
                #print(username)
                #print(password)
            user.save()
           # user = authenticate(username=username)
            #if user is not None:
            print("Logging out and logging in!!")
            #logout(request)
            #user = authenticate(username=username)
            #print(user.username)
            logout(request)
            user = authenticate(username=username)
            #print(username)
            if user is not None:
                login(request, user)
            #print("should have logged out")
            #thename = get_name(request)
            #print(thename)
            #print("is none")
            #username = form.username
            #password = form.password
            #user = authenticate(username=username, password=password)
            #print("what")
            return redirect('lastpage')
    
    form = UserCreateForm()
    #ndacheck = NdaCheckBox()
    return render(request, 'invite/register.html', {'userform':form, 'date':datetime.now().date(), 'message':'','name': name})
