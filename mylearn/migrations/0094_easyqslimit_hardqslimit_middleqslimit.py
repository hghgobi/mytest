# Generated by Django 2.1.7 on 2020-12-04 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0093_hardkilleronoff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Easyqslimit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(default=1)),
                ('num', models.IntegerField(default=1)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hardqslimit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(default=1)),
                ('num', models.IntegerField(default=1)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Middleqslimit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(default=1)),
                ('num', models.IntegerField(default=1)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
