from django.db import models

# Create your models here.

class about(models.Model):
    """docstring for about."""


    vision = models.TextField()
    mission = models.TextField()
    image = models.ImageField(upload_to='about/')
    def __init__(self, arg):
        super(about, self).__init__()
        self.arg = arg
