# Generated by Django 3.0.8 on 2020-07-21 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.URLField(null=True),
        ),
    ]
