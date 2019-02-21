# Generated by Django 2.0.5 on 2019-01-19 16:21

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albam',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=100)),
                ('description', models.TextField(db_column='description')),
                ('updated_at', models.DateField(db_column='updated_at', default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('photo', models.ImageField(db_column='file', upload_to='albam/images/')),
                ('title', models.CharField(db_column='title', max_length=100)),
                ('creater', models.CharField(db_column='creater', max_length=250)),
                ('created_at', models.DateField(db_column='created_at', default=datetime.datetime(2019, 1, 19, 16, 21, 50, 890717, tzinfo=utc))),
                ('albam_id', models.ForeignKey(db_column='albam_id', on_delete=django.db.models.deletion.CASCADE, to='Albam.Albam')),
            ],
        ),
    ]