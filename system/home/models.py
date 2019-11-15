from django.db import models

# Create your models here.
class home(models.Model):
    # location =
    all = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)


    def __str__(self):
        return str(self.id)
