# Generated by Django 5.0.1 on 2024-02-09 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0022_blog_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='likes',
        ),
    ]
