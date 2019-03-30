from django.db import models
from django.utils import timezone

import datetime

# Create your models here.

class Albam(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=100, db_column='name')
    description = models.TextField(db_column='description')
    btn_class = models.CharField(max_length=100, db_column='btn_class')
    updated_at = models.DateTimeField(default=timezone.now, db_column='updated_at')

    def __str__(self):
        return self.name

    def diff_date(self):
        diff_words = ['日前', '時間前', '分前', '秒前']

        now = timezone.now()
        diff_date = now - self.updated_at
        diff_hours = diff_date.seconds / 60 / 60
        diff_minutes = diff_date.seconds / 60

        if (6 < diff_date.days):
            return self.updated_at.date()
        elif (0 < diff_date.days):
            return str(diff_date.days) + diff_words[0]
        elif (0 < diff_hours):
            return str(diff_hours) + diff_words[1]
        elif (0 < diff_minutes):
            return str(diff_minutes) + diff_words[2]
        elif (0 < diff_date.seconds):
            return str(diff_date.seconds) + diff_words[3]

class Photo(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    albam_id = models.ForeignKey(Albam, on_delete=models.CASCADE, db_column='albam_id')
    photo = models.ImageField(
        upload_to='images/Albam/',
        db_column='photo',
    )
    title = models.CharField(max_length=100, db_column='title')
    creater = models.CharField(max_length=250, db_column='creater')
    created_at = models.DateField(default=timezone.now, db_column='created_at')
    twitter_account = models.CharField(max_length=250, default=None, db_column='account')

    def __str__(self):
        return self.title

    def diff_date(self):
        diff_words = '日前'

        now = timezone.now().date()
        diff_date = now - self.created_at

        if (6 < diff_date.days):
            return self.created_at
        elif (0 < diff_date.days):
            return str(diff_date.days) + diff_words
