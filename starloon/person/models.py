from django.db import models
from django.template.defaultfilters import slugify
from datetime import date
from django.contrib.auth.models import User
from PIL import Image


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
    coverUrl = models.ImageField(null=True, upload_to='person-cover/%Y/%m/%d')
    personImage = models.ImageField(null=True, upload_to='person-profile/%Y/%m/%d')
    detailscouverture = models.ImageField(null=True, upload_to='person-detailcouverture/%Y/%m/%d')

    def save(self, *args, **kwargs):
        super().save()

        pers = Image.open(self.personImage.path)
        cover = Image.open(self.coverUrl.path)
        detail = Image.open(self.detailscouverture.path)

        if pers.height > 100 or pers.width > 100:
            new_pers = (100, 100)
            pers.thumbnail(new_pers)
            pers.save(self.personImage.path)

        if cover.height > 250 or cover.width > 400:
            new_cover = (250, 400)
            cover.thumbnail(new_cover)
            cover.save(self.coverUrl.path)

        if detail.height > 250 or detail.width > 150:
            new_detail = (200, 150)
            detail.thumbnail(new_detail)
            detail.save(self.detailscouverture.path)
        
        
    
    def __str__(self):
        return self.surname 

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.fullName)
        super(Person, self).save(*args, **kwargs)

    
