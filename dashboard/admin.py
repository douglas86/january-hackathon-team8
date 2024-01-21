from django.contrib import admin
from .models import UpcomingBill, Category


# Register your models here.
@admin.register(UpcomingBill)
class UpcomingBillAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'due_date', 'amount', 'status')


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name_of_category', 'icon')
