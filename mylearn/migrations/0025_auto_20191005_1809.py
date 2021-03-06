# Generated by Django 2.1.7 on 2019-10-05 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0024_newnames'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yuxitestcount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zid', models.IntegerField()),
                ('jid', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('time', models.DateField(auto_now=True)),
                ('count', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
        migrations.AlterModelOptions(
            name='yuxiname',
            options={'ordering': ['-time']},
        ),
        migrations.AddField(
            model_name='yuxiname',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
