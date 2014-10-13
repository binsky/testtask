from django.shortcuts import render

def home_method(request):
    return render(request, 'index.html', {})