# Generated by Django 3.1 on 2020-08-23 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.CharField(choices=[('1톤', '1톤'), ('2.5톤', '2.5톤'), ('5톤', '5톤'), ('기타', '기타')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('owner_name', models.CharField(max_length=20)),
                ('tel', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=50)),
                ('registration_number', models.CharField(max_length=10, unique=True)),
                ('registration_date', models.DateField()),
                ('workers_count', models.IntegerField()),
                ('is_matching', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('tel', models.CharField(max_length=11)),
                ('joined_date', models.DateField(auto_now_add=True)),
                ('is_agree_terms', models.BooleanField(default=False)),
                ('is_agree_third_party', models.BooleanField(default=False)),
                ('is_agree_marketing', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MoveFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_agree_public', models.BooleanField(default=False)),
                ('professional_level', models.IntegerField(choices=[(5, '매우만족'), (4, '만족'), (3, '보통'), (2, '불만족'), (1, '매우불만족')])),
                ('price_level', models.IntegerField(choices=[(5, '매우만족'), (4, '만족'), (3, '보통'), (2, '불만족'), (1, '매우불만족')])),
                ('kindness_level', models.IntegerField(choices=[(5, '매우만족'), (4, '만족'), (3, '보통'), (2, '불만족'), (1, '매우불만족')])),
                ('is_revisit', models.BooleanField(default=False)),
                ('contract_price', models.IntegerField()),
                ('move_date', models.DateField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('content', models.CharField(max_length=300)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.company')),
            ],
        ),
        migrations.CreateModel(
            name='RequestHouseMove',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_address', models.CharField(max_length=50)),
                ('starting_floors', models.IntegerField()),
                ('destination_address', models.CharField(max_length=50)),
                ('destination_floors', models.IntegerField()),
                ('move_date', models.DateField()),
                ('is_storage', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.customer')),
                ('feedback', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.movefeedback')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyCarCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.car')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.company')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='cars_count',
            field=models.ManyToManyField(through='common.CompanyCarCount', to='common.Car'),
        ),
    ]
