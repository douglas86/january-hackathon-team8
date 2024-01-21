from django import forms
from .models import UpcomingBill, Income, Expense


class EditDashboardForm(forms.ModelForm):
    class Meta:
        model = UpcomingBill
        fields = ['title', 'amount', 'due_date']
        widgets = {'due_date': forms.DateInput(attrs={'type': 'date'})}

        labels = {
            'due_date': 'Due Date:',
        }


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['source', 'amount', 'frequency', 'date_received', 'description']
        widgets = {'date_received': forms.DateInput(attrs={'type': 'date'})}

        labels = {
            'date_received': 'Date received:',
        }


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['source', 'category', 'amount', 'date_received', 'description']
        widgets = {'date_received': forms.DateInput(attrs={'type': 'date'})}

        labels = {
            'date_received': 'Date received:'
        }
