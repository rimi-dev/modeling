# Generated by Django 3.1 on 2020-08-25 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20200824_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movefeedback',
            name='content',
            field=models.CharField(max_length=1000),
        ),
    ]
