# Generated by Django 2.1.7 on 2020-12-03 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0091_hardqsname'),
    ]

    operations = [
        migrations.AddField(
            model_name='hardqs',
            name='answerdetail',
            field=models.ImageField(default=33, upload_to='hardquestions'),
            preserve_default=False,
        ),
    ]
