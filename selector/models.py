from django.db import models

# Create your models here.

class song(models.Model):
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

    def empty_check_limited(self):
        if self.limited is None:
            return True
        else:
            return False
    
    class Meta:
        db_table = 'song_list'
        unique_together = (("title", "difficulty", "attribute"))
