# Generated by Django 2.0.6 on 2018-06-27 21:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]