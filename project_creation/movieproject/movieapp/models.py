from django.db import models

class Movie(models.Model):
    name=models.CharField(max_length=250)
    year=models.IntegerField()
    desc=models.TextField()
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name