from django.shortcuts import render

def welcome(request):
    return render(request, 'invite/index.html', {})

def access(request):
    return render(request, 'invite/generic.html', {})

