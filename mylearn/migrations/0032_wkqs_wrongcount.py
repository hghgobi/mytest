# Generated by Django 2.1.7 on 2019-10-13 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0031_xxqs_ornot'),
    ]

    operations = [
        migrations.AddField(
            model_name='wkqs',
            name='wrongcount',
            field=models.IntegerField(default=0),
        ),
    ]
