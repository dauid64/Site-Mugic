# Generated by Django 2.2 on 2022-08-26 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mugic', '0002_auto_20220825_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='video_url',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
