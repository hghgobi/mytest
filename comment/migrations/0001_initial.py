# Generated by Django 2.1.7 on 2019-04-05 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('text', models.TextField()),
                ('comment_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(max_length=100)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType')),
            ],
        ),
    ]
