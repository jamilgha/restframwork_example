# Generated by Django 4.1.7 on 2024-04-01 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_slider_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider_home',
            name='slider_tag',
            field=models.CharField(help_text='Movie tags', max_length=500, null=True),
        ),
    ]