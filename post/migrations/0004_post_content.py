# Generated by Django 4.2.1 on 2023-06-03 21:47

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default='python.html'),
            preserve_default=False,
        ),
    ]
