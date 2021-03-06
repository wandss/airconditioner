# Generated by Django 4.0.4 on 2022-04-12 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0002_controlprofile_delete_remote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='controlprofile',
            name='settings',
        ),
        migrations.RemoveField(
            model_name='controlprofile',
            name='swing',
        ),
        migrations.AddField(
            model_name='controlprofile',
            name='options',
            field=models.CharField(choices=[('2-Step', 'Two Step'), ('Fast', 'Fast'), ('Confort', 'Confort'), ('Single User', 'Single User'), ('Quiet', 'Quiet'), ("D'light Cool", 'Dlight Cool'), ('Virus Doctor', 'Virus Doctor')], default='Quiet', max_length=12),
        ),
        migrations.AlterField(
            model_name='controlprofile',
            name='mode',
            field=models.CharField(choices=[('Auto', 'Auto'), ('Cool', 'Cool'), ('Dry', 'Dry'), ('Fan', 'Fan')], default='Cool', max_length=4),
        ),
        migrations.AlterField(
            model_name='controlprofile',
            name='temperature',
            field=models.CharField(choices=[('16', 'Sixteen'), ('17', 'Seventeen'), ('18', 'Eighteen'), ('19', 'Nineteen'), ('20', 'Twenty'), ('21', 'Twenty One'), ('22', 'Twenty Two'), ('23', 'Twenty Three'), ('24', 'Twenty Four'), ('25', 'Twenty Five'), ('26', 'Twenty Six'), ('27', 'Twenty Seven'), ('28', 'Twenty Eight'), ('29', 'Twenty Nine'), ('30', 'Thirty')], default='25', max_length=2),
        ),
    ]
