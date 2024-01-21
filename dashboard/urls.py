from . import views
from django.urls import path

urlpatterns = [
    path('delete_modal/<int:pk>/', views.DeleteDashboard.as_view(), name='delete_model'),
    path('edit_model/<int:pk>', views.Dashboard.as_view(), name='edit_model'),
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('new_bill/', views.Dashboard.as_view(), name='new_bill'),
    path('income/', views.IncomeListView.as_view(), name='income'),
    path('edit_income/<int:pk>', views.IncomeListView.as_view(), name='edit_income'),
    path('delete_income/<int:pk>', views.DeleteIncomeView.as_view(), name='delete_income'),
    path('filter_income/', views.IncomeListView.as_view(), name='filter_income'),
    path('cur_converter/', views.CurConverter.as_view(), name='cur_converter'),

]
