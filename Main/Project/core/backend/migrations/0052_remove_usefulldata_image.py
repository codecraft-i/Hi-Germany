# Generated by Django 5.0.1 on 2024-02-14 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0051_usefulldata_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usefulldata',
            name='image',
        ),
    ]