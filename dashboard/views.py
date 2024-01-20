from django.shortcuts import render
from django.views.generic import ListView
from .models import UpcomingBill


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
