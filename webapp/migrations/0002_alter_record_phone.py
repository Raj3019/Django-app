# Generated by Django 5.0.2 on 2024-02-18 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
