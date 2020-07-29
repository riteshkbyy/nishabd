# Generated by Django 3.0.8 on 2020-07-28 04:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(upload_to='', verbose_name='Profile Picture: ')),
                ('birth_date', models.DateField(verbose_name='Date of Birth: ')),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('u', 'Prefer not to say')], max_length=1, verbose_name='Gender')),
                ('marital_status', models.CharField(choices=[('m', 'Married'), ('u', 'Unmarried'), ('d', 'Divorced'), ('w', 'Widowed')], max_length=1, verbose_name='Marital status: ')),
                ('about', models.CharField(max_length=300, verbose_name='About me: ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]