# Generated by Django 3.0.1 on 2020-07-05 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200704_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.ForeignKey(default='No tag', on_delete=django.db.models.deletion.CASCADE, to='blog.Tag'),
        ),
    ]
