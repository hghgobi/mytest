# Generated by Django 2.1.7 on 2020-03-01 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0064_datirecord'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datirecord',
            options={'ordering': ['time']},
        ),
        migrations.AddField(
            model_name='datirecord',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
