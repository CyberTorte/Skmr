# Generated by Django 2.1.7 on 2019-03-30 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Albam', '0008_auto_20190331_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='twitter_account',
            field=models.CharField(blank=True, db_column='account', default=None, max_length=250, null=True),
        ),
    ]
