# Generated by Django 2.1.7 on 2020-12-10 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0096_draws'),
    ]

    operations = [
        migrations.AddField(
            model_name='hardqs',
            name='sum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hardqs',
            name='sum4',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hardqs',
            name='killer',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='hardqs',
            name='killer4',
            field=models.CharField(max_length=5000),
        ),
    ]