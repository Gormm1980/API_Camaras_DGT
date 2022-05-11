# Generated by Django 4.0.4 on 2022-05-11 10:50

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
            ],
            bases=(models.Model, django.db.models.fields.related.ForeignKey),
        ),
        migrations.CreateModel(
            name='TarfficCamera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('url', models.URLField(verbose_name='')),
            ],
            bases=(models.Model, django.db.models.fields.related.ForeignKey),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='location',
            name='TarfficCamera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tarfficcamera'),
        ),
    ]
