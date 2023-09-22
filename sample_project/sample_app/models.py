from django.db import models


# Create your models here.

class place(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pictures')
    description = models.TextField()

    def __str__(self):
        return self.name

class team(models.Model):
    name = models.CharField(max_length=250)
    profile_picture=models.ImageField(upload_to='Avatar')
    description=models.TextField()

    def __str__(self):
        return self.name

