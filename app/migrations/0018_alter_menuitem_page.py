# Generated by Django 4.2.7 on 2023-11-24 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_menuitem_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.page'),
        ),
    ]
