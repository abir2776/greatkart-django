# Generated by Django 3.2.11 on 2022-08-25 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_location', '0001_initial'),
        ('store', '0008_alter_productgallery_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_location.location'),
        ),
    ]