# Generated by Django 5.0 on 2024-03-23 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=200)),
                ('Last_Name', models.CharField(max_length=200)),
                ('Age', models.CharField(max_length=200)),
                ('Qualification', models.CharField(max_length=200)),
                ('DOB', models.DateField()),
                ('Language_Known', models.CharField(max_length=200)),
            ],
        ),
    ]