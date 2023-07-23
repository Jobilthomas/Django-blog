from django.db import models
from django.urls import reverse

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=30)
    
        
    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="post_images/")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="posts")
    excerpt = models.CharField(max_length=400)
    content = models.TextField()
    slug = models.SlugField(default="", null=False, db_index=True)
    tags = models.ManyToManyField(Tag)
    
    def get_absolute_url(self):
        return (reverse("post-detail-page", args=[self.slug]))
    
    def __str__(self):
        return f"{self.title} [{self.date}]"
    

class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    comment = models.TextField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
