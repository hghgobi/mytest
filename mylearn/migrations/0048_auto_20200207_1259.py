# Generated by Django 2.1.7 on 2020-02-07 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0047_classnotes0'),
    ]

    operations = [
        migrations.AddField(
            model_name='xxqs',
            name='id1',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='xxqs',
            name='id2',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]