from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UpcomingBill(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    due_date = models.DateField(format("%Y-%m-%d"), null=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.BooleanField(default=False, editable=False)

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return self.title


class Income(models.Model):
    FREQUENCY_CHOICES = [
        ('monthly', 'Monthly'),
        ('annual', 'Annual'),
        ('one-time', 'One-time'),
        ('weekly', 'Weekly'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)
    date_received = models.DateField(format("%Y-%m-%d"), null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.source} - {self.amount} ({self.frequency})"


class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_received = models.DateField(format("%Y-%m-%d"), null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['date_received']

    def __str__(self):
        return f"{self.source} - {self.amount}"


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    icon = models.ImageField(upload_to='images/category_icons', default='none.jpeg')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
