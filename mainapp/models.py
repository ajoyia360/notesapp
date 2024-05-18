from django.db import models

# Note Model


class NoteModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    screen_shoot=models.ImageField(upload_to='screenshots')
    def __str__(self):
        return self.title