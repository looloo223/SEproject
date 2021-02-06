from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html')

def operation(request):
    return render(request, 'app/operation.html')

