from django.db import models
from cloudinary.models import CloudinaryField

# Note Model


class NoteModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    screen_shoot = CloudinaryField('image', null=True, blank=True)
    def __str__(self):
        return self.title