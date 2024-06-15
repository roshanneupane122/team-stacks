# Generated by Django 5.0.6 on 2024-06-15 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('contact_number', models.CharField(max_length=15)),
                ('photo', models.ImageField(upload_to='hotel_photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('contact_number', models.CharField(max_length=15)),
                ('photo', models.ImageField(upload_to='vehicle_photos/')),
            ],
        ),
    ]
