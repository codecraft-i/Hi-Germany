# Generated by Django 5.0.1 on 2024-02-10 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0031_extrablog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrablog',
            name='exLinkAdress',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='extrablog',
            name='exLinkName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]