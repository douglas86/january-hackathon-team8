# Generated by Django 5.0.1 on 2024-01-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_alter_upcomingbill_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingbill',
            name='due_date',
            field=models.DateField(null=True, verbose_name='%Y-%m-%d'),
        ),
    ]
