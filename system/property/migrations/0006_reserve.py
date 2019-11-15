# Generated by Django 2.2.6 on 2019-11-04 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_remove_property_property_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('notes', models.TextField()),
            ],
        ),
    ]
