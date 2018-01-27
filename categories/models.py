from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify   #for slug

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 255)
    slug = models.SlugField(allow_unicode = True, unique=True)
    description = models.CharField(max_length = 255)
    image = models.ImageField(upload_to = 'categories/images')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self,**kwargs):
        return reverse('categories:detail',kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']