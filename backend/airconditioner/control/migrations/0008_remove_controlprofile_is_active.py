# Generated by Django 4.0.4 on 2022-04-14 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0007_controlprofile_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='controlprofile',
            name='is_active',
        ),
    ]
