# Generated by Django 2.1.2 on 2018-10-30 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20181030_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, upload_to='main/static/media/images/', width_field=150),
        ),
    ]