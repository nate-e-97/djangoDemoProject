# Generated by Django 4.2.3 on 2023-07-18 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=32)),
                ('lastName', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=32)),
                ('zipCode', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=2)),
            ],
        ),
    ]
