# Generated by Django 2.1.7 on 2020-03-01 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0065_auto_20200301_1006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datirecord',
            options={'ordering': ['costtime']},
        ),
        migrations.RemoveField(
            model_name='datirecord',
            name='time',
        ),
        migrations.AddField(
            model_name='daticontrol',
            name='seconds',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datirecord',
            name='costtime',
            field=models.IntegerField(default=0),
        ),
    ]
