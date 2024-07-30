from django.db import models

# Simplified model to store image details
class Image(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField()
    photographer = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
