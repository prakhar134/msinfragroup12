from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    level_no = models.IntegerField(default=0)
    target = models.FloatField(default=0.0)
    Ac_No = models.IntegerField(default=0)
    bank = models.CharField(max_length=200)
    IFSC = models.CharField(max_length=11)
    Pan_no = models.CharField(max_length=10)

    def __str__(self):
        return self.name