from . import views
from django.urls import path

urlpatterns = [
    path('edit_model/<int:pk>', views.Dashboard.as_view(), name='edit_model'),
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('new_bill', views.Dashboard.as_view(), name='new_bill'),

]
