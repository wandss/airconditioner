# Generated by Django 4.0.4 on 2022-04-12 11:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('temperature', models.CharField(max_length=3)),
                ('mode', models.CharField(max_length=10)),
                ('swing', models.CharField(max_length=10)),
                ('settings', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Remote',
        ),
    ]