# Generated by Django 4.2.4 on 2023-08-03 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='No_of_guests',
            field=models.SmallIntegerField(default=6),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Inventory',
            field=models.SmallIntegerField(default=5),
        ),
    ]
