# Generated by Django 2.0.3 on 2018-04-07 22:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20180407_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
