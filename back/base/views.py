from django.shortcuts import render

def index(request):
   
   context = {}
   return render(request, 'base/index.html', context)

def registration(request):
   page_type = 'registration'
   
   context = {'page_type': page_type}
   return render(request, 'base/auth.html', context)

def login(request):
   page_type = 'login'
   
   context = {'page_type': page_type}
   return render(request, 'base/auth.html', context)
