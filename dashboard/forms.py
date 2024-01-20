from django import forms
from .models import UpcomingBill


class EditDashboardForm(forms.ModelForm):
    class Meta:
        model = UpcomingBill
        fields = ['title', 'amount', 'due_date']
        widgets = {'due_date': forms.DateInput(attrs={'type': 'date'})}