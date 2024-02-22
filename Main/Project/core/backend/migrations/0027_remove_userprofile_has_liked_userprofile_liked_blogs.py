# Generated by Django 5.0.1 on 2024-02-09 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0026_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='has_liked',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='liked_blogs',
            field=models.ManyToManyField(blank=True, to='backend.blog'),
        ),
    ]