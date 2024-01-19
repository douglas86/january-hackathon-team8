from django.contrib import admin
from .models import UpcomingBill


# Register your models here.
@admin.register(UpcomingBill)
class UpcomingBillAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'due_date', 'amount', 'status')

# admin.site.register(UpcomingBillAdmin)
