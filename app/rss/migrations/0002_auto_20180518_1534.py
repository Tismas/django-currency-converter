# Generated by Django 2.0.5 on 2018-05-18 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangerate',
            name='value',
            field=models.FloatField(),
        ),
    ]
