# Generated by Django 4.1.5 on 2023-02-12 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_autor_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_foto',
            field=models.ImageField(null=True, upload_to='images/post_foto'),
        ),
    ]