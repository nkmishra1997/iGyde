from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'landing/index.html', {})

def home(request):
    return render(request, 'landing/home.html', {})