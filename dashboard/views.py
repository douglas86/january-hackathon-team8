from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views import View
from .models import UpcomingBill
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


# Create your views here.
class Dashboard(View):
    template_name = 'dashboard/index.html'

    def get(self, request, *args, **kwargs):
        bills = UpcomingBill.objects.filter(user=request.user)
        form = [EditDashboardForm(instance=bill) for bill in bills]
        # form = EditDashboardForm(request.POST)
        my_list = zip(form, bills)
        context = {'my_list': my_list}
        return render(request, self.template_name, context)
        # if self.request.user.is_authenticated:
        #     return UpcomingBill.objects.filter(user=self.request.user)
        # else:
        #     return 'none'

    def post(self, request, pk, *args, **kwargs):
        bill = get_object_or_404(UpcomingBill, pk=pk)
        form = EditDashboardForm(request.POST, instance=bill)
        try:
            if form.is_valid():
                new_bill = form.save(commit=False)
                # new_bill.due_date = form.due_date.strftime('%Y-%m-%d')
                new_bill.save()
                return redirect('dashboard')
            else:
                print(form.errors)
                return render(request, self.template_name)
        except Exception as e:
            print(e)

    # def get_context_data(self, **kwargs):
    #     return {'bills': self.get_queryset()}


class EditDashboardForm(forms.ModelForm):
    class Meta:
        model = UpcomingBill
        fields = '__all__'
        widgets = {'due_date': forms.DateInput(attrs={'type': 'date'})}


class EditDashboard(View):
    """
    View to edit the dashboard of the titled document
    """
    # model = UpcomingBill
    # form_class = EditDashboardForm
    # template_name = 'dashboard/index.html'
    # success_url = '/'

    # def get(self, request, pk):
    #     UpcomingBill.objects.get(pk=pk)
    #     return JsonResponse()

    # def post(self, request, pk, *args, **kwargs):
    #     form = EditDashboardForm(request.POST)
    #     # bill = get_object_or_404(UpcomingBill, pk=pk)
    #     try:
    #         if form.is_valid():
    #             new_bill = form.save(commit=False)
    #             new_bill.user = request.user
    #             new_bill.title = form.title
    #             new_bill.amount = form.amount
    #             new_bill.due_date = form.due_date.strftime('%Y-%m-%d')
    #             new_bill.save()
    #             return redirect('')
    #         else:
    #             print(form.errors)
    #     except Exception as e:
    #         print(e)
