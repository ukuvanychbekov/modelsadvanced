# Generated by Django 3.2 on 2022-08-18 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20220818_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='card_number',
            field=models.CharField(max_length=100),
        ),
    ]