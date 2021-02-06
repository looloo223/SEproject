from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html')

def health(request):
    return render(request, 'app/health.html')
    
def contact(request):
    return render(request, 'app/contact.html')
