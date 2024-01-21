from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from .models import UpcomingBill
from .forms import EditDashboardForm
from django.shortcuts import get_object_or_404


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

    # def delete(self, request, pk, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         delete_bill = get_object_or_404(UpcomingBill, pk=pk)
    #         delete_bill.delete()
    #         return redirect(request, self.template_name)
