# Generated by Django 4.2.7 on 2023-11-27 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_menuitem_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='delete_date',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='delete_date',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='delete_date',
        ),
        migrations.RemoveField(
            model_name='page',
            name='delete_date',
        ),
    ]
