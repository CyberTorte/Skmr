from django.db import models

# Create your models here.

class Song(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    title = models.CharField(max_length=100, db_column='title')
    attribute = models.CharField(max_length=50, db_column='attribute', default='all')
    difficulty = models.CharField(max_length=50, db_column='difficulty')
    level = models.IntegerField(db_column='level')
    artist = models.CharField(max_length=100, db_column='artist')
    style = models.CharField(max_length=50, db_column='style', default='5')
    limited = models.CharField(max_length=50, db_column='limited', null=True, blank=True, default=None)
    party = models.BooleanField(db_column='party', default=False)

    def __str__(self):
        return self.title + "：" + self.difficulty + "：" + self.attribute

    def check_exist_attribute(self, value=None):
        if value is not None:
            if self.attribute == value:
                return True
            else:
                return False
        else:
            return False

    def check_exist_difficulty(self, value=None):
        if value is not None:
            if self.difficulty == value:
                return True
            else:
                return False
        else:
            return False

    def check_exist_limited(self, value=None):
        if value is None:
            if self.limited is None:
                return True
            else:
                return False
        elif self.limited == value:
            return True

        else:
            return False

    def check_empty_limited(self):
        if self.limited is None:
            return True
        else:
            return False
    
    class Meta:
        db_table = 'song_list'
        unique_together = (("title", "difficulty", "attribute"))
