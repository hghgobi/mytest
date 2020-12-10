# Generated by Django 2.1.7 on 2020-12-10 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0098_hardqsrecord_ornot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jifeng',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sum', models.IntegerField(default=0)),
                ('time', models.DateTimeField(auto_now=True)),
                ('clas', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='Jifengrecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
                ('num', models.IntegerField()),
                ('reason', models.CharField(max_length=50)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]
