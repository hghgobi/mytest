# Generated by Django 2.1.7 on 2020-12-10 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0100_jifengrecord_clas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jifengrecord',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
