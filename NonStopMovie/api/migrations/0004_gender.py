# Generated by Django 4.1 on 2022-08-19 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_movie_link_play_alter_movie_movie_votes_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='gender',
            fields=[
                ('gender_id', models.IntegerField(help_text='gender id', primary_key=True, serialize=False)),
                ('gender_name', models.CharField(help_text='gender name', max_length=500)),
            ],
        ),
    ]