from django.db import models


class Staff(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)
    age = models.SmallIntegerField()
    phone = models.SmallIntegerField()

    def __str__(self):
        return f"{self.surname} {self.name}"