
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def africa(request):
    return render(request, "loja.html")