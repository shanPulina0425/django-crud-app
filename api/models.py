from django.db import models

# Create your models here.


class User(models.Model):

    age = models.IntegerField()
    name = models.CharField(max_length=200)

    def _str_(self):

        return self.name
