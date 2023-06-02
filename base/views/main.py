from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def instructions_view(request):
   return render(request, 'base/main_pages/instructions.html')

def medals_view(request):
   return render(request, 'base/main_pages/medals.html')

def sorting_view(request):
   return render(request, 'base/main_pages/sorting.html')