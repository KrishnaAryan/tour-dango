from django.db import models

# Create your models here.
class Photo(models.Model):
    photo=models.ImageField(upload_to='photo/')
    date=models.DateField()
    location=models.CharField(max_length=200,blank=True, null=True)
    