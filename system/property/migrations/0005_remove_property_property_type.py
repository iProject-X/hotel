# Generated by Django 2.2.6 on 2019-11-04 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20191104_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='property_type',
        ),
    ]
