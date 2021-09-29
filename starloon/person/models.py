from django.db import models
from django.template.defaultfilters import slugify
from datetime import date


# Create your models here.
class Person(models.Model):
    fullName = models.CharField(max_length=500)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=25, null = True)
    bio = models.CharField(max_length=300)
    age = models.IntegerField()
    slug = models.SlugField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    birth_date = models.DateField(blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    published = models.BooleanField(default=False)
    coverUrl = models.URLField(null=True, blank=True)

    
    def __str__(self):
        return self.surname 

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.fullName)
        super(Person, self).save(*args, **kwargs)