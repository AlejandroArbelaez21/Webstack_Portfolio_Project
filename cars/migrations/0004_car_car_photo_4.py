# Generated by Django 3.0.7 on 2021-04-28 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20210428_0434'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_photo_4',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
