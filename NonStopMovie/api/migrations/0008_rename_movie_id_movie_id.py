# Generated by Django 4.1 on 2022-08-19 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_movie_moviegender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='movie_id',
            new_name='id',
        ),
    ]
