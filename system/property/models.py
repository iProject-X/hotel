from django.db import models


# Create your models here.

#property_type = (
#    ('sale' , "sale"),
#    ('rent' , "rent")
#)

class Property(models.Model):
    name = models.CharField(max_length=50)
    #property_type = models.CharField(choices=property_type , max_length=10)
    price = models.PositiveIntegerField()   
    area = models.DecimalField(decimal_places=2 ,max_digits=8 )
    beds_number = models.PositiveIntegerField()
    baths_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property/', null=True)

    def __str__(self):
        return self.name

class homeImages(models.Model):
    image = models.ImageField(upload_to='homeImages/', null=True)
    def __str__(self):
        return self.image


class Reserve(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    notes  = models.TextField()

    def __str__(self):
        return self.name
