# Generated by Django 4.1.5 on 2023-01-16 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='cover',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
