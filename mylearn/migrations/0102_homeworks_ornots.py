# Generated by Django 2.1.7 on 2020-12-13 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0101_auto_20201210_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeworks',
            name='ornots',
            field=models.CharField(default='已发放', max_length=200),
            preserve_default=False,
        ),
    ]