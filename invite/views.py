from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import InterestForm, UserCreateForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import AccessCode

from django.http import HttpResponseRedirect

from datetime import datetime

from django.contrib.auth.forms import UserCreationForm

def welcome(request):
    return render(request, 'invite/index.html', {})

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

def access(request):
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
                    return redirect('/login')
                else:
                    return HttpResponseRedirect("/register")
                    #return redirect('/register')
                    #return render(request, 'invite/newuser.html', {})
            else:
                return render(request, 'invite/invalid.html', {})
            
    else:
        form = InterestForm()
    return render(request, 'invite/access.html', {'form': form})


#@login_required(login_url='/access')
def nda(request):
    #print(email)
    if (request.GET.get('successbutton')):
        return render(request, 'invite/lastpage.html', {})
    return render(request, 'invite/nda.html', {'time':datetime.now().date(),})

@login_required(login_url='/login')
def lastpage(request):
    return render(request, 'invite/lastpage.html', {})

#@login_required(login_url='/access')
def logout_view(request):
    logout(request)
    return redirect('welcome')

def register_user(request):
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
            user = form.save()
            username = user.username
            if not User.objects.filter(username=username).exists():
                #print(username)
                form = UserCreateForm()
                return render(request, 'invite/register.html', {'userform':form, 'date':datetime.now().date(), 'message':"username already taken!",})
            password = user.password
                #print(username)
                #print(password)
            authenticate(username=username)
            #username = form.username
            #password = form.password
            #user = authenticate(username=username, password=password)
            #print("what")
            return redirect('lastpage')
    
    form = UserCreateForm()
    #ndacheck = NdaCheckBox()
    return render(request, 'invite/register.html', {'userform':form, 'date':datetime.now().date(), 'message':'',})
