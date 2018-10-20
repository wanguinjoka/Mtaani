from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Kijiji(models.Model):

    location = models.CharField(max_length=100)
    description = models.TextField()
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.location

class News(models.Model):
    tag = models.CharField(max_length=100)
    cation = models.CharField(max_length = 100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    kijiji = models.ForeignKey(Kijiji, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag

class Business(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    contacts = models.CharField(max_length=11)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    kijiji = models.ForeignKey(Kijiji, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Police(models.Model):
    station = models.CharField(max_length=100)
    contacts = models.CharField(max_length=11)
    kijiji = models.ForeignKey(Kijiji, on_delete=models.CASCADE)

    def __str__(self):
        return self.station

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    contacts = models.CharField(max_length=11)
    kijiji = models.ForeignKey(Kijiji, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
