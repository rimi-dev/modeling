# Generated by Django 3.1 on 2020-08-26 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20200825_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companycarcount',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
