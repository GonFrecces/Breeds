# Generated by Django 3.0.14 on 2022-08-04 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breeds',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Raza', models.CharField(max_length=100)),
                ('ImageURL', models.CharField(max_length=200)),
            ],
        ),
    ]