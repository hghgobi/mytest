# Generated by Django 2.1.7 on 2019-04-06 06:35

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_time']},
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]