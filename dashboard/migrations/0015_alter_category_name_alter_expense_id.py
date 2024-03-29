# Generated by Django 5.0.1 on 2024-01-21 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_category_expense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
