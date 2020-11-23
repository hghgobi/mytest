# Generated by Django 2.1.7 on 2020-11-23 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0078_auto_20201003_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Getflowerrecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('hwname', models.CharField(max_length=500)),
                ('flower', models.IntegerField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('reason', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='Homeworks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('hwname', models.CharField(max_length=500)),
                ('time', models.IntegerField()),
                ('ornot', models.CharField(max_length=200)),
                ('clas', models.IntegerField()),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='Homeworksid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='yuxinamezk',
            options={'ordering': ['fs', 'count', 'costtime']},
        ),
        migrations.RemoveField(
            model_name='xxqs23',
            name='answer',
        ),
        migrations.AddField(
            model_name='rankxhl',
            name='jid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rankxhl',
            name='zid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='xxqs23',
            name='answers',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='yuxinamezk',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='xxqs2',
            name='answer',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='xxqs22',
            name='answer',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='xxqs24',
            name='answer',
            field=models.CharField(max_length=500),
        ),
    ]
