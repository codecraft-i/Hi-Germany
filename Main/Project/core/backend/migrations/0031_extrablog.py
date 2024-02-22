# Generated by Django 5.0.1 on 2024-02-10 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0030_delete_extrablog'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='backend/static/Home/Assets/Images/BlogImages')),
                ('description', models.TextField()),
                ('exLinkName', models.CharField(max_length=255)),
                ('exLinkAdress', models.CharField(max_length=2000)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='backend.blog')),
            ],
        ),
    ]
