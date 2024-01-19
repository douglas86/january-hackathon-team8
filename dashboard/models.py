from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UpcomingBill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    due_date = models.DateField(auto_now=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-due_date']

    def __str__(self):
        return self.title
