# Generated by Django 3.0.8 on 2020-07-23 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_auto_20200723_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]
