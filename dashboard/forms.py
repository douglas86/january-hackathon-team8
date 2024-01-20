from django import forms
from .models import UpcomingBill


class EditDashboardForm(forms.ModelForm):
    class Meta:
        model = UpcomingBill
        fields = '__all__'
        widgets = {'due_date': forms.DateInput(attrs={'type': 'date'})}