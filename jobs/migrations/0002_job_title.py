# Generated by Django 2.0.6 on 2018-06-28 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
    ]
