# Generated by Django 2.1.7 on 2020-02-09 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0051_xxqs2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xxqs22',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num0', models.IntegerField()),
                ('num1', models.IntegerField()),
                ('yunsuan', models.IntegerField()),
                ('answer', models.IntegerField(default=0)),
                ('ornot', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Xxqs23',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num0', models.IntegerField()),
                ('num1', models.IntegerField()),
                ('yunsuan', models.IntegerField()),
                ('answer', models.IntegerField(default=0)),
                ('ornot', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Xxqs24',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num0', models.IntegerField()),
                ('num1', models.IntegerField()),
                ('yunsuan', models.IntegerField()),
                ('answer', models.IntegerField(default=0)),
                ('ornot', models.IntegerField(default=0)),
            ],
        ),
    ]
