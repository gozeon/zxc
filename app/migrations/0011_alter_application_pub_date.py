# Generated by Django 4.2.7 on 2023-11-14 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_application_create_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='date published'),
        ),
    ]
