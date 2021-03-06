# Generated by Django 2.1.7 on 2020-12-24 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0112_hweveryday_hweverydayrecord_studentids'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paotui',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('studentname', models.CharField(max_length=50)),
                ('ornot', models.CharField(max_length=50)),
                ('ornots', models.CharField(max_length=50)),
                ('clas', models.IntegerField(default=3)),
                ('time', models.DateTimeField(auto_now=True)),
                ('num', models.IntegerField()),
                ('jihui', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]
