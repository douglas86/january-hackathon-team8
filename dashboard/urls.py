from . import views
from django.urls import path

from .views import Dashboard

urlpatterns = [
    path('edit_model/<int:pk>', views.EditDashboard.as_view(), name='edit_model'),
    path('', Dashboard.as_view(), name='dashboard'),
]
