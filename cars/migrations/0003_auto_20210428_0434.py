# Generated by Django 3.0.7 on 2021-04-28 04:34

import ckeditor.fields
from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20210427_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='car',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Seat Heating', 'Seat Heating'), ('Alarm System', 'Alarm System'), ('ParkAssist', 'ParkAssist'), ('Power Steering', 'Power Steering'), ('Reversing Camera', 'Reversing Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Wind Deflector', 'Wind Deflector'), ('Bluetooth Handset', 'Bluetooth Handset')], max_length=255),
        ),
    ]
