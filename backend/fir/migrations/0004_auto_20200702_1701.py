# Generated by Django 3.0.6 on 2020-07-02 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0003_fir_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fir',
            name='complaintype',
            field=models.TextField(),
        ),
    ]
