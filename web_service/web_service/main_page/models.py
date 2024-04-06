from django.db import models

# Create your models here.
class Recieve(models.Model):
    name = models.CharField(max_length = 45)
    device = models.IntegerField()

    def __str__(self):
        return self.name