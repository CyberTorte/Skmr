# Generated by Django 2.1.7 on 2019-03-30 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Albam', '0010_card_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='comment',
            field=models.TextField(blank=True, db_column='comment', default=None, null=True),
        ),
    ]
