# Generated by Django 2.1.7 on 2019-10-28 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0040_auto_20191019_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wkqs3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zid', models.IntegerField()),
                ('jid', models.IntegerField()),
                ('questiontext', models.ImageField(upload_to='questions')),
                ('questionanswer1', models.CharField(max_length=50)),
                ('questionanswer2', models.CharField(max_length=50)),
                ('questionanswer3', models.CharField(max_length=50)),
                ('wrongcount', models.IntegerField(default=0)),
                ('category', models.IntegerField(default=0)),
            ],
        ),
    ]
