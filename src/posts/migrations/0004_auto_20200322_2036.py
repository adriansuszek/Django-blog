# Generated by Django 3.0.3 on 2020-03-22 19:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_views_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='pole123',
        ),
        migrations.AlterField(
            model_name='post',
            name='overview',
            field=ckeditor.fields.RichTextField(),
        ),
    ]