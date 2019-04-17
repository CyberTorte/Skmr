from django.db import models
from django.utils import timezone

import datetime, math

import local_settings as settings

# Create your models here.

class Albam(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=100, db_column='name')
    description = models.TextField(db_column='description')
    btn_class = models.CharField(max_length=100, db_column='btn_class')
    order_rule = models.BooleanField(default=False, db_column='order_rule')
    jumbotron_image = models.ForeignKey('Picture', on_delete=models.CASCADE, default=None, blank=True, null=True, db_column="jumbotron")
    updated_at = models.DateTimeField(default=timezone.now, db_column='updated_at')

    def __str__(self):
        return self.name

    def diff_date(self):
        diff_words = ['日前', '時間前', '分前', '秒前']

        now = timezone.now()
        diff_date = now - self.updated_at
        diff_hours = math.floor(diff_date.seconds / 60 / 60)
        diff_minutes = math.floor(diff_date.seconds / 60)

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
        else:
            return '今'

class Card(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    albam = models.ForeignKey(Albam, on_delete=models.CASCADE, db_column='albam')
    title = models.CharField(max_length=100, db_column='title')
    comment = models.TextField(default=None, blank=True, null=True, db_column='comment')
    creater = models.CharField(max_length=250, db_column='creater')
    created_at = models.DateField(default=timezone.now, db_column='created_at')
    twitter_account = models.BigIntegerField(default=None, blank=True, null=True, db_column='account')

    def __str__(self):
        return self.title

    def diff_date(self):
        diff_words = '日前'

        now = timezone.now().date()
        diff_date = now - self.created_at

        if (6 < diff_date.days):
            return self.created_at
        elif (1 <= diff_date.days):
            return str(diff_date.days) + diff_words
        else:
            return '今'

    def get_profile_image(self):
        if self.twitter_account:
            api = settings.get_twitter_api()
            account_data = api.GetUser(user_id = self.twitter_account)
            
            if account_data.default_profile_image:
                return None
            else:
                return account_data.profile_image_url_https.replace('_normal')

        else:
            return None


class Picture(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    card = models.ForeignKey(Card, on_delete=models.CASCADE, db_column='card')
    picture = models.ImageField(
        upload_to='images/Albam/',
        db_column='photo',
    )

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

    def diff_date(self):
        diff_words = '日前'

        now = timezone.now().date()
        diff_date = now - self.created_at

        if (6 < diff_date.days):
            return self.created_at
        elif (0 < diff_date.days):
            return str(diff_date.days) + diff_words
