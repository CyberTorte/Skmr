from django.db import models
from django.utils import timezone

# Create your models here.

class Albam(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=100, db_column='name')
    description = models.TextField(db_column='description')
    updated_at = models.DateField(default=timezone.now, db_column='updated_at')

    def __str__(self):
        return self.name

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
        return title