# Generated by Django 2.1.7 on 2020-11-26 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0081_lucky_uselucky'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='uselucky',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
