from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Django Model of post database
    Code has been written by instructions from
    Code Institute module I think therefore i blog
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        """Orders posts by date created using descending order"""
    ordering = ["-created_on"]

    def __str__(self):
        """Magic Method, returns a string representation of an object"""
        return self.title

    def number_of_likes(self):
        """Helper method, returns total count of likes on a post"""
        return self.likes.count()


class Comment(models.Model):
    """
    Django model of comments
    Code has been written by instructions from
    Code Institute module I think therefore i blog
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """Shows order of comments"""
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
