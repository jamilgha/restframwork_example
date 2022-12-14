# Generated by Django 4.1 on 2022-08-19 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_movie_movie_poster_alter_movie_movie_votes_avg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='Link_play',
            field=models.URLField(help_text='Downloads and Stream Movie', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_votes_count',
            field=models.IntegerField(help_text='Movie Budget'),
        ),
    ]
