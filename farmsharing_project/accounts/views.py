from django.shortcuts import render

# Create your views here.

def land_new(request):
    return render(request, 'land_new.html')