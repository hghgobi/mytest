# Generated by Django 2.1.7 on 2020-12-14 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0104_auto_20201213_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Limitin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id0', models.IntegerField()),
                ('id1', models.IntegerField()),
                ('id2', models.IntegerField()),
            ],
        ),
    ]
