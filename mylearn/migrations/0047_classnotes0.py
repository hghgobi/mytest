# Generated by Django 2.1.7 on 2020-02-07 11:32

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylearn', '0046_xhl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classnotes0',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notename', models.CharField(max_length=200)),
                ('notecontent', ckeditor_uploader.fields.RichTextUploadingField()),
                ('notetime', models.DateTimeField(auto_now_add=True)),
                ('noteupdatetime', models.DateTimeField(auto_now=True)),
                ('readed_num', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]