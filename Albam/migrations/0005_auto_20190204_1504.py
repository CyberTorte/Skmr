# Generated by Django 2.0.5 on 2019-02-04 06:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Albam', '0004_auto_20190122_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albam',
            name='updated_at',
            field=models.DateTimeField(db_column='updated_at', default=django.utils.timezone.now),
        ),
    ]
