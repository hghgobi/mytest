# Generated by Django 2.1.7 on 2020-12-01 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0084_setgoodns_ornot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Luckys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('name', models.CharField(max_length=500)),
                ('reason', models.CharField(max_length=500)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]
