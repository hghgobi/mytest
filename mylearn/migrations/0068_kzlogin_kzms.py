# Generated by Django 2.1.7 on 2020-03-12 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0067_zbhf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kzlogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Kzms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('idNumber', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('addressDetail', models.CharField(max_length=500)),
                ('addressCode', models.CharField(max_length=500)),
            ],
        ),
    ]
