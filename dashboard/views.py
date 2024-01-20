from django import forms
from django.shortcuts import render, redirect
from django.views import View
from .models import UpcomingBill
from django.shortcuts import get_object_or_404


# Create your views here.
class Dashboard(View):
    """
    This view is responsible for sending and receiving from a database
    """
    template_name = 'dashboard/index.html'

    def get(self, request, *args, **kwargs):
        bills = UpcomingBill.objects.filter(user=request.user)
        form = [EditDashboardForm(instance=bill) for bill in bills]
        my_list = zip(form, bills)
        context = {'my_list': my_list}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        bill = get_object_or_404(UpcomingBill, pk=pk)
        form = EditDashboardForm(request.POST, instance=bill)
        try:
            if form.is_valid():
                new_bill = form.save(commit=False)
                new_bill.save()
                return redirect('dashboard')
            else:
                print(form.errors)
                return render(request, self.template_name)
        except Exception as e:
            print(e)


class EditDashboardForm(forms.ModelForm):
    class Meta:
        model = UpcomingBill
        fields = '__all__'
        widgets = {'due_date': forms.DateInput(attrs={'type': 'date'})}
