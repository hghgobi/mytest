# Generated by Django 2.1.7 on 2020-11-27 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0083_auto_20201127_0618'),
    ]

    operations = [
        migrations.AddField(
            model_name='setgoodns',
            name='ornot',
            field=models.IntegerField(default=0),
        ),
    ]