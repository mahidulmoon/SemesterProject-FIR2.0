# Generated by Django 3.0.6 on 2020-07-02 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complainerinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fathername', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('contact', models.CharField(max_length=15)),
            ],
        ),
    ]
