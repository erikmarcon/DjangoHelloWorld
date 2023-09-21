from django.db import models

# Create your models here.

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=32)
    zipcode = models.CharField(max_length=16)
    property = models.CharField(max_length=128)
    email = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
