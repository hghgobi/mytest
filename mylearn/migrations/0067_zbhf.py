# Generated by Django 2.1.7 on 2020-03-02 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0066_auto_20200301_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zbhf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id0', models.IntegerField()),
                ('id1', models.IntegerField()),
                ('ornot', models.IntegerField(default=0)),
            ],
        ),
    ]
