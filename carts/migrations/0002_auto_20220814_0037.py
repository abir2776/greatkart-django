# Generated by Django 3.2.11 on 2022-08-13 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
