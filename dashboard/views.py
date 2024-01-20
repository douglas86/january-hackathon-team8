from django import forms
from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from .models import UpcomingBill
from django.views.decorators.csrf import csrf_protect

# Create your views here.
class Dashboard(ListView):
    template_name = 'dashboard/index.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return UpcomingBill.objects.filter(user=self.request.user)
        else:
            return 'none'

    def get_context_data(self, **kwargs):
        return {'bills': self.get_queryset()}


class EditDashboardForm(forms.ModelForm):
    class Meta:
        model = UpcomingBill
        fields = '__all__'


class EditDashboard(UpdateView):
    """
    View to edit the dashboard of the titled document
    """
    model = UpcomingBill
    form_class = EditDashboardForm
    template_name = 'dashboard/index.html'
    success_url = '/'

    def get_object(self, queryset=None):
        return UpcomingBill.objects.get(pk=self.kwargs['pk'])
