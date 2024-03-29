# Generated by Django 5.0 on 2023-12-27 12:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_delete_usefulldata'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UsefullData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='backend/static/Home/Assets/Images/BlogImages')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tags', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
