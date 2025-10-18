from django.shortcuts import render

def home(request):
    return render(request, 'html/home.html')

def index(request):
    return render(request, 'html/index.html')

