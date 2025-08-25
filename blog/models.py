from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from tinymce.models  import HTMLField
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    content_field = HTMLField()
    created_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    categories = models.ManyToManyField(Category, related_name="posts")
    image = models.OneToOneField('ImageModel', on_delete=models.SET_NULL, null=True, blank=True, related_name="article")

    def __str__(self):
        return self.title

class ImageModel(models.Model):
    title = models.CharField( max_length=50)
    image = models.ImageField( upload_to='images/', null=True, blank=True)
    uploaded_at = models.DateTimeField( default=timezone.now)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on "{self.post.title}"'
