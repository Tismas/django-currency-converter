# Generated by Django 2.0.5 on 2018-05-18 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_currency', models.CharField(max_length=30)),
                ('target_currency', models.CharField(max_length=30)),
                ('value', models.IntegerField()),
                ('timestamp', models.DateField()),
            ],
        ),
    ]
