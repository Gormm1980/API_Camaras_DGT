# Generated by Django 4.0.4 on 2022-05-11 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_location_tarfficcamera_delete_post_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TarfficCamera',
            new_name='TrafficCamera',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='TarfficCamera',
            new_name='TrafficCamera',
        ),
    ]
