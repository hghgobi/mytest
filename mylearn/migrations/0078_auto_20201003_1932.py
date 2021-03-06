# Generated by Django 2.1.7 on 2020-10-03 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0077_auto_20201001_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sdengji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=200)),
                ('srank', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sshuliang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zid', models.IntegerField()),
                ('jid', models.IntegerField()),
                ('seta', models.IntegerField()),
                ('setb', models.IntegerField()),
                ('setc', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='yuxinamezk',
            options={'ordering': ['fs', 'costtime']},
        ),
        migrations.AddField(
            model_name='zktishu',
            name='id4',
            field=models.IntegerField(default=0),
        ),
    ]
