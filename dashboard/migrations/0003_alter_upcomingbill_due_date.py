# Generated by Django 5.0.1 on 2024-01-19 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_upcomingbill_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingbill',
            name='due_date',
            field=models.DateField(),
        ),
    ]
