# Generated by Django 5.0.2 on 2024-02-19 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0002_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('No_of_guests', models.SmallIntegerField(default=6)),
                ('BookingDate', models.DateField()),
            ],
        ),
    ]