# Generated by Django 4.2.7 on 2023-11-15 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_page_menuitem_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='link',
        ),
    ]
