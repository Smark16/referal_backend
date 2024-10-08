# Generated by Django 5.1 on 2024-08-12 11:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=100)),
                ('TelephoneNumber', models.PositiveBigIntegerField()),
                ('Age', models.PositiveIntegerField()),
                ('Gender', models.CharField(max_length=6)),
                ('MaritalStatus', models.CharField(max_length=10)),
                ('EmailAddress', models.EmailField(blank=True, max_length=254, null=True)),
                ('Nationality', models.CharField(max_length=100)),
                ('Ugandan_Identification_Number', models.CharField(blank=True, max_length=100, null=True)),
                ('Refugee_Number', models.CharField(blank=True, max_length=100, null=True)),
                ('settlement', models.CharField(blank=True, max_length=255, null=True)),
                ('district_city', models.CharField(blank=True, max_length=255, null=True)),
                ('subcounty_division', models.CharField(blank=True, max_length=255, null=True)),
                ('parish_ward', models.CharField(blank=True, max_length=255, null=True)),
                ('village_cell_zone', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_bussiness', models.CharField(max_length=255)),
                ('year_of_establishment', models.PositiveIntegerField()),
                ('type_of_bussiness', models.CharField(max_length=255)),
                ('Business_location', models.CharField(max_length=255)),
                ('total_employees', models.IntegerField()),
                ('revenue_per_annum', models.DecimalField(decimal_places=2, max_digits=12)),
                ('location_address', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_for_additional_services', models.CharField(max_length=255)),
                ('confirmation', models.BooleanField()),
                ('modules_interested_in', models.ManyToManyField(to='referal.modules')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
