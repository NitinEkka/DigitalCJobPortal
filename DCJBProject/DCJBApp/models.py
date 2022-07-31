from django.db import models

class JB_Info(models.Model):
    location = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    exp = models.IntegerField()
    pay = models.IntegerField()
    contact = models.IntegerField()
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.skill
