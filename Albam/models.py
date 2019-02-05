from django.db import models
from django.utils import timezone

from dateutil.relativedelta import relativedelta

# Create your models here.

class Albam(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=100, db_column='name')
    description = models.TextField(db_column='description')
    updated_at = models.DateTimeField(default=timezone.now, db_column='updated_at')

    def __str__(self):
        return self.name

    def diff_date(self):
        diff_words = ['日前', '時間前', '分前', '秒前']

        now = timezone.now()
        diff_delta = relativedelta(now, self.updated_at)

        if (6 < diff_delta.days):
            return self.updated_at.date()
        elif (0 < diff_delta.days):
            return str(diff_delta.days) + diff_words[0]
        elif (0 < diff_delta.hours):
            return str(diff_delta.hours) + diff_words[1]
        elif (0 < diff_delta.minutes):
            return str(diff_delta.minutes) + diff_words[2]
        elif (0 < diff_delta.seconds):
            return str(diff_delta.seconds) + diff_delta[3]

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

    def __str__(self):
        return self.title
