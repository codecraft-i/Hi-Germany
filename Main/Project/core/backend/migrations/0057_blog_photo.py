# Generated by Django 5.0.1 on 2024-02-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0056_blog_description_f_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='photo',
            field=models.ImageField(default='backend/static/Home/Assets/Images/BlogImages/ger-imTh_jkyd7QU.jpg', upload_to='backend/static/Home/Assets/Images/BlogImages'),
        ),
    ]
