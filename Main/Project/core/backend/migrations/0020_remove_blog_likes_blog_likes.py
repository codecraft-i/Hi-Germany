# Generated by Django 5.0.1 on 2024-02-07 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_blog_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='likes',
        ),
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
