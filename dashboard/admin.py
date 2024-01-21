from django.contrib import admin
from .models import UpcomingBill, Category, Expense


# Register your models here.
@admin.register(UpcomingBill)
class UpcomingBillAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'due_date', 'amount', 'status')


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon')


@admin.register(Expense)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('id', 'source', 'category', 'amount', 'date_received', 'description')
