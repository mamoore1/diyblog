from django.db import models


# Create your models here.
class Blogger(models.Model):
    """Model representing an author"""
    username = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000, help_text='Enter a brief description of the blogger')


class BlogPost(models.Model):
    """Model representing a blog post"""
    post_date = models.DateField()
    author = models.ForeignKey(Blogger, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, help_text="Enter the text of the blog post")


class Comment(models.Model):
    blogpost = models.ForeignKey(BlogPost, on_delete=models.SET_NULL, null=True)
    post_time = models.DateTimeField()
    commenter = models.CharField(max_length=100, help_text="Enter your name")
    text = models.TextField(max_length=1000, help_text="Enter your comment")
