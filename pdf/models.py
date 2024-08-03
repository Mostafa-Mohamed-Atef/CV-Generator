from django.db import models

# Create your models here.
class Profile(models.Model):
    def __str__(self) -> str:
        return self.id
    name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    phone = models.CharField(max_length=225)
    summary = models.TextField()
    linkedin = models.CharField(max_length=225)
    university = models.CharField(max_length=225)
    work = models.CharField(max_length=225)
    skill = models.CharField(max_length=225)