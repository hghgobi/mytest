# Generated by Django 2.1.7 on 2019-04-11 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0011_homeworksum_lastlogintime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homeworksum',
            old_name='lastlogintime',
            new_name='lasttime',
        ),
    ]
