# Generated by Django 2.1.7 on 2020-12-15 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0105_limitin'),
    ]

    operations = [
        migrations.AddField(
            model_name='homewrecord',
            name='clas',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
