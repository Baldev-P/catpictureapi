from django.db import models
# Create your models here.


class CatPicture(models.Model):
    image = models.ImageField(upload_to='cat_pics/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
