from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import UpcomingBill, Income
from .forms import EditDashboardForm, IncomeForm, IncomeFilterForm

# Create your views here.
class Dashboard(View):
    """
    This view is responsible for sending and receiving from a database
    """
    template_name = 'dashboard/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            new_form = EditDashboardForm(request.POST)
            bills = UpcomingBill.objects.filter(user=request.user)
            form = [EditDashboardForm(instance=bill) for bill in bills]
            my_list = zip(form, bills)
            context = {'my_list': my_list, 'form': new_form}
            return render(request, self.template_name, context)
        return render(request, self.template_name)


    def post(self, request, pk=None, *args, **kwargs):
        if pk:
            bill = get_object_or_404(UpcomingBill, pk=pk)
            form = EditDashboardForm(request.POST, instance=bill)
        else:
            form = EditDashboardForm(request.POST)

        try:
            if form.is_valid():
                new_bill = form.save(commit=False)
                new_bill.user = request.user
                new_bill.save()
                return redirect('dashboard')
            else:
                print(form.errors)
                return render(request, self.template_name)
        except Exception as e:
            print(e)


class DeleteDashboard(DeleteView):
    """
    This view is responsible for deleting an entry from a database
    """
    model = UpcomingBill
    template_name = 'dashboard/index.html'
    success_url = reverse_lazy('dashboard')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.success_url)


@method_decorator(login_required, name='dispatch')
class IncomeListView(View):
    template_name = 'dashboard/income.html'

    def get(self, request ):
        
        filter_form = IncomeFilterForm(request.GET)
        income_list = Income.objects.filter(user=request.user)

        if filter_form.is_valid():
            source = filter_form.cleaned_data['source']
            if source:
               print(source)
               income_list = income_list.filter(source__in=source)

            frequency = filter_form.cleaned_data['frequency']
            if frequency:
                income_list = income_list.filter(frequency=frequency)

            date_to = filter_form.cleaned_data['date_to']
            date_from = filter_form.cleaned_data['date_from']
            if date_from and date_to:
                income_list = income_list.filter(date_received__range=[date_from, date_to])
            elif date_from:
                income_list = income_list.filter(date_received__gte=date_from)
            elif date_to:
                income_list = income_list.filter(date_received__lte=date_to)

            total_amount = sum(income.amount for income in income_list)


        form = IncomeForm(request.GET)
        forms = [IncomeForm(instance=income) for income in income_list]

        my_list = zip(forms, income_list)
        context = {'my_list': my_list, 'form': form, 'filter_form': filter_form, 'total_amount': total_amount}
        return render(request, self.template_name, context)


    def post(self, request, pk=None):
        if pk:
            income = get_object_or_404(Income, pk=pk, user=request.user)
            form = IncomeForm(request.POST, instance=income)
        else:
            form = IncomeForm(request.POST)

        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('income')
        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class DeleteIncomeView(View):
    def post(self, request, pk):
        income = get_object_or_404(Income, pk=pk, user=request.user)
        income.delete()
        return redirect('income')