from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.
class Dashboard(ListView):
    queryset = 'none'
    template_name = 'dashboard/index.html'
