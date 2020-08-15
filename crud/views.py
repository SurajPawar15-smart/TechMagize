from django.shortcuts import render
from django.http import HttpResponse
def about(request):
   return render(request, 'about.html')
def category(request):
    return render(request, 'category.html')
def contact(request):
    return render(request, 'contact.html')
def index(request):
    return render(request, 'index.html')
def elements(request):
    return render(request, 'elements.html')
def single(request):
    return render(request, 'single.html')

