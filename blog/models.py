from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


class Author(models.Model):
    name = models.CharField(max_length=110)
    age = models.SmallIntegerField()

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=255, unique=True, null=True, blank=True)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    create_at = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-view', args=[str(self.id)])