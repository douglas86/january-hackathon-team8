from django import forms
from .models import UpcomingBill, Income


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

class IncomeFilterForm(forms.Form):
    source = forms.MultipleChoiceField(
        choices=[(source, source) for source in Income.objects.values_list('source', flat=True).distinct()],
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    frequency = forms.ChoiceField(
        choices=[(None, 'None')] + list(Income.FREQUENCY_CHOICES),
        required=False,
    )

    date_from = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
    )

    date_to = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
    )



class IncomeFilterForm(forms.Form):
    source = forms.MultipleChoiceField(
        choices=[(source, source) for source in Income.objects.values_list('source', flat=True).distinct()],
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    frequency = forms.ChoiceField(
        choices=[(None, 'None')] + list(Income.FREQUENCY_CHOICES),
        required=False,
    )

    date_from = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
    )

    date_to = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
    )

