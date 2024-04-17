from functools import wraps
from .models import Tournament

import random
import os


def slug_generator(string):
    return '-'.join(string.lower().split(' '))


def checking_slug(slug):
    while Tournament.objects.filter(slug=slug).exists():
        slug += str(random.randrange(10000))
    return slug


def generate_slug(form):
    # create massive for slug
    slug = []

    # create slug
    if form.cleaned_data.get('category'):
        slug.append(str(form.cleaned_data['category']))

    if form.cleaned_data.get('gender'):
        slug.append(str(form.cleaned_data['gender']))

    if form.cleaned_data.get('weight'):
        slug.append(str(form.cleaned_data['weight']))

    if form.cleaned_data.get('year'):
        slug.append(str(form.cleaned_data['year']))

    slug = ' '.join(slug)

    return slug
