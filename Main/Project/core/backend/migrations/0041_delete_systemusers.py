# Generated by Django 5.0.1 on 2024-02-10 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0040_alter_systemusers_country'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SystemUsers',
        ),
    ]
