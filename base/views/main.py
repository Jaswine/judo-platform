from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

"""
   Страница с выводом инструкций пользователям
"""
def instructions_view(request):
   return render(request, 'base/main_pages/instructions.html')

"""
   Страница с выводом турниров и медалистов в разных категориях
"""
def medals_view(request):
   return render(request, 'base/main_pages/medals.html')

"""
   Страница с выводом турниров и сортировки спортсменов 
"""
def sorting_view(request):
   return render(request, 'base/main_pages/sorting.html')