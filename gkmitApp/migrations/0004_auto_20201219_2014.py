# Generated by Django 3.1.2 on 2020-12-19 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gkmitApp', '0003_auto_20201219_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]