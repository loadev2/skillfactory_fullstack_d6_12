import uuid

from django.db import models

# Create your models here.
class Shelter(models.Model):
    title = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.title

class Pets(models.Model):
    TYPES = [
        (1, 'dogs'),
        (2, 'cats'),
        (3, 'parrots'),
    ]
    name = models.TextField()
    type = models.PositiveSmallIntegerField(default=1, choices=TYPES)
    breed = models.TextField(default='')
    datearrival = models.DateField()
    host = models.TextField(default='')
    image = models.ImageField(upload_to='pet_avatars/%Y/%m/%d', blank=True)
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

