# Generated by Django 3.2.11 on 2022-08-20 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_reviewrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewrating',
            name='rating',
            field=models.FloatField(default=1.0),
        ),
    ]
