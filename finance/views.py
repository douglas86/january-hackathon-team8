from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView


# Create your views here.
class Finance(ListView):
    queryset = 'none'
    template_name = 'finance/index.html'
