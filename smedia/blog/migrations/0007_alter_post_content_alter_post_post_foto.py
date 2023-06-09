# Generated by Django 4.1.5 on 2023-02-14 22:29

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_post_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(help_text='max 1000 characters', max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_foto',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/post_foto'),
            preserve_default=False,
        ),
    ]
