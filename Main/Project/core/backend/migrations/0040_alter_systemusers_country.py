# Generated by Django 5.0.1 on 2024-02-10 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0039_rename_systemuser_systemusers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemusers',
            name='country',
            field=models.CharField(blank=True, choices=[('UZ', 'Uzbekistan'), ('DE', 'Germany'), ('IN', 'India'), ('CN', 'China'), ('GB', 'United Kingdom')], max_length=2),
        ),
    ]