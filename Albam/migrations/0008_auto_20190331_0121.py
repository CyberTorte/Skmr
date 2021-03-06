# Generated by Django 2.1.7 on 2019-03-30 16:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Albam', '0007_photo_twitter_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='title', max_length=100)),
                ('creater', models.CharField(db_column='creater', max_length=250)),
                ('created_at', models.DateField(db_column='created_at', default=django.utils.timezone.now)),
                ('twitter_account', models.CharField(db_column='account', default=None, max_length=250)),
                ('albam', models.ForeignKey(db_column='albam', on_delete=django.db.models.deletion.CASCADE, to='Albam.Albam')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('picture', models.ImageField(db_column='photo', upload_to='images/Albam/')),
                ('card', models.ForeignKey(db_column='card', on_delete=django.db.models.deletion.CASCADE, to='Albam.Card')),
            ],
        ),
        migrations.RemoveField(
            model_name='photo',
            name='twitter_account',
        ),
    ]
