# Generated by Django 2.1.7 on 2019-10-10 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0029_xxqs'),
    ]

    operations = [
        migrations.AddField(
            model_name='xxqs',
            name='answer',
            field=models.IntegerField(default=0),
        ),
    ]
