# Generated by Django 4.1.5 on 2023-02-14 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_content_alter_post_post_foto'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='posts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
    ]
