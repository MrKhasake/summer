from django.shortcuts import render, get_object_or_404
from .models import Entrepreneurship, Finance

# Create your views here.
def detail(request, slug):
    manager = get_object_or_404(Entrepreneurship, slug=slug)
    return render(request, 'post-page.html', {'manager':manager})


def show(request, slug):
    bought = get_object_or_404(Finance, slug=slug)
    return render(request, 'post-page2.html', {'bought':bought})