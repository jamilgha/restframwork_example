# Generated by Django 4.1 on 2022-08-19 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_poster',
            field=models.ImageField(blank=True, help_text='Movie poster', upload_to='movie_poster'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_votes_avg',
            field=models.DecimalField(decimal_places=2, help_text='Movie Budget', max_digits=8),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_votes_count',
            field=models.DecimalField(decimal_places=2, help_text='Movie Budget', max_digits=8),
        ),
    ]
