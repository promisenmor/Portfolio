from django.shortcuts import render
from .models import Project


def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolioApp/portfolio.html', {'projects': projects})