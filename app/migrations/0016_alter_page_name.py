# Generated by Django 4.2.7 on 2023-11-15 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_remove_menuitem_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
