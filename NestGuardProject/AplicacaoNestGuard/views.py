from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import NestGuard

# Create your views here.
def homepage(request):
    context = {}
    dadosEmpresa = NestGuard.objects.all()
    context["dadosEmpresa"] = dadosEmpresa
    return render(request, 'homepage.html', context)