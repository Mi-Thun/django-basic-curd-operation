from django.db import models

class User(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)

    def __str__(self):
        return self.name
