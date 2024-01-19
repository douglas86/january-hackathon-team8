from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UpcomingBill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    due_date = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)
