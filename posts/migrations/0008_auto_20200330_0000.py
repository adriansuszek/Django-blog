# Generated by Django 3.0.3 on 2020-03-29 22:00

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20200329_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='overview',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
