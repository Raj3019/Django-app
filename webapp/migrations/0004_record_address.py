# Generated by Django 5.0.2 on 2024-02-18 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_record_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='address',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
