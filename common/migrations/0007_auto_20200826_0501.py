# Generated by Django 3.1 on 2020-08-26 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_auto_20200826_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='joined_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='movefeedback',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]