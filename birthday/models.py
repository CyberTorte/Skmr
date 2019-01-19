from django.db import models

# Create your models here.

class Photo(models.Model):
    # 画像のパス
    path = models.CharField(max_length=200, db_column='path')
    # 種類
    kind = models.CharField(max_length=100, db_column='name')
    # 連番
    serial = models.IntegerField(db_column='serial')
    # 対象の人
    person = models.CharField(max_length=100, db_column='person')
    # 開催年
    year = models.IntegerField(db_column='year')

    def __str__(self):
        return self.kind + str(self.serial) + self.person

    class Meta:
        db_table = 'old_photo'