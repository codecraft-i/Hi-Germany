# Generated by Django 5.0.2 on 2024-02-17 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0062_usefulldata_description_f_body_de_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrausefull',
            name='description_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='extrausefull',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='extrausefull',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='extrausefull',
            name='description_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='extrausefull',
            name='link_name_de',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='extrausefull',
            name='link_name_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='extrausefull',
            name='link_name_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='extrausefull',
            name='link_name_uz',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]