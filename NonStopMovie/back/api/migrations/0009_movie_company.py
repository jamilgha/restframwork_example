# Generated by Django 4.1.7 on 2024-04-01 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_rename_movie_id_movie_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='movie_company',
            fields=[
                ('company_id', models.AutoField(help_text='movie_id', primary_key=True, serialize=False)),
                ('Movie_id', models.IntegerField(help_text='movie_id')),
                ('company_name', models.CharField(help_text='Company Name', max_length=500)),
            ],
        ),
    ]
