# Generated by Django 5.0.1 on 2024-02-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0048_messageusefull'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visasdata',
            name='colors',
            field=models.CharField(choices=[('Blue', 'Blue'), ('Purple', 'Purple'), ('Yellow', 'Yellow'), ('Pink', 'Pink')], max_length=255, null=True),
        ),
    ]
