# Generated by Django 4.1.7 on 2024-04-01 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_movie_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_company',
            name='company_id',
            field=models.UUIDField(help_text='movie_id', primary_key=True, serialize=False),
        ),
    ]
