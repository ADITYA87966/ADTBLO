# Generated by Django 3.2.17 on 2023-03-06 09:02

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Content',
            field=tinymce.models.HTMLField(),
        ),
    ]