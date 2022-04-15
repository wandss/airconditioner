# Generated by Django 4.0.4 on 2022-04-12 03:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Remote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('temperature', models.CharField(max_length=3)),
                ('mode', models.CharField(max_length=10)),
                ('swing', models.CharField(max_length=10)),
                ('settings', models.CharField(max_length=10)),
            ],
        ),
    ]