# Generated by Django 5.0.1 on 2024-02-15 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0058_rename_description_usefulldata_description_f_body_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField()),
            ],
        ),
    ]
