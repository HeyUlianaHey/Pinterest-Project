from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from pins.models import Pin


@login_required
def home(request):
    pins = Pin.objects.all()
    context = {'pins': pins[:49]}
    return render(request, 'home.html', context)


@login_required
def search(request):
    query = request.GET.get('q')
    pins = Pin.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    ).all()
    context = {'pins': pins[:49]}
    return render(request, 'home.html', context)
