# Generated by Django 3.1.3 on 2020-12-03 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20201201_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='contact',
            field=models.CharField(default='contact', max_length=32),
        ),
    ]