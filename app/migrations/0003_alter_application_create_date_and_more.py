# Generated by Django 4.2.7 on 2023-11-14 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_application_create_date_application_delete_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='application',
            name='delete_date',
            field=models.DateTimeField(default=None, verbose_name='date deleted'),
        ),
    ]
