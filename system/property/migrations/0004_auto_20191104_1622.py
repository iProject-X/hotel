# Generated by Django 2.2.6 on 2019-11-04 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_homeimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeimages',
            name='image',
            field=models.ImageField(null=True, upload_to='homeImages/'),
        ),
    ]
