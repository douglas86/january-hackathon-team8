from django import forms
from .models import UpcomingBill, Income, Expense, Category


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


class ExspenseFilterForm(forms.Form):
  
    source = forms.MultipleChoiceField(
        choices=[(source, source) for source in Expense.objects.values_list('source', flat=True).distinct()],
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
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



class ExpenseForm(forms.ModelForm):
    new_category = forms.CharField(max_length=50, required=False, label='New Category')
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label='--- Select Existing Category ---',
        required=False,
        label='Existing Categories'
    )

    class Meta:
        model = Expense
        fields = ['source', 'amount', 'date_received', 'description']

        widgets = {
            'date_received': forms.DateInput(attrs={'type': 'date'})
        }

        labels = {
            'date_received': 'Date received'
        }

    def clean(self):
        cleaned_data = super().clean()
        new_category = cleaned_data.get('new_category')
        existing_category = cleaned_data.get('category')

        if not new_category and not existing_category:
            raise forms.ValidationError('Please select an existing category or enter a new one.')

        return cleaned_data