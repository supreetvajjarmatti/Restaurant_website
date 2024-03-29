# Generated by Django 3.0.5 on 2024-01-09 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('datetime', models.DateTimeField()),
                ('no_of_people', models.IntegerField()),
                ('special_request', models.TextField()),
            ],
        ),
    ]
