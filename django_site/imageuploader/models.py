from django.db import models


class ImageModel(models.Model):
    image = models.ImageField(upload_to='blog_uploads/', null=True)

