from . import views
from django.urls import path

from .views import Dashboard

urlpatterns = [
    path('edit/', views.EditDashboard.as_view(), name='edit'),
    path('', Dashboard.as_view(), name='dashboard'),
]
