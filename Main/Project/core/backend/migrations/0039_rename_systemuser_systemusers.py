# Generated by Django 5.0.1 on 2024-02-10 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0038_systemuser_gender'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SystemUser',
            new_name='SystemUsers',
        ),
    ]