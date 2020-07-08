# Generated by Django 3.0.1 on 2020-07-03 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200703_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='image',
            field=models.ImageField(default='media/tags/images/Metallica_-_Metallica_cover.jpg', upload_to='media/tags/images'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='image',
            field=models.ImageField(default='media/writers/images/default.jpg', upload_to='media/writers/images'),
        ),
    ]
