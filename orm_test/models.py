from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)
    age = models.PositiveIntegerField()
    email = models.EmailField(null=True, blank=True)
    bio = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    body = models.TextField()
    author = models.ForeignKey(Author, related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.URLField(null=True, blank=True)
    published = models.BooleanField()

    def __str__(self):
        return f"{self.title} ({self.author})"