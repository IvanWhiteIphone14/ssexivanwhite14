# Generated by Django 4.2.5 on 2023-10-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_car_photo_car_main_photo_carphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='short_info',
            field=models.CharField(default='short info', max_length=1000),
        ),
    ]
