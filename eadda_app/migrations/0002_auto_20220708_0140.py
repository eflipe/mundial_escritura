# Generated by Django 3.2.5 on 2022-07-08 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eadda_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stories',
            name='author',
        ),
        migrations.DeleteModel(
            name='SongInfo',
        ),
        migrations.DeleteModel(
            name='Stories',
        ),
    ]
