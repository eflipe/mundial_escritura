# Generated by Django 3.2.5 on 2022-07-13 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eadda_app', '0004_auto_20220713_1146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='songinfo',
            options={'verbose_name_plural': 'Songs Info'},
        ),
        migrations.AlterModelOptions(
            name='stories',
            options={'verbose_name_plural': 'Stories'},
        ),
        migrations.AlterField(
            model_name='songinfo',
            name='song_lyrics',
            field=models.TextField(max_length=5000),
        ),
    ]
