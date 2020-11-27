from django.db import models
from django.urls import reverse


# Create your models here.
class Blogger(models.Model):
    """Model representing an author"""
    username = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000, help_text='Enter a brief description of the blogger')

    def __str__(self):
        """String for representing the Model object"""
        return f'{self.username}'

    def get_absolute_url(self):
        """Returns the url to access a particular blogger instance"""
        return reverse('blogger-detail', args=[str(self.id)])


class BlogPost(models.Model):
    """Model representing a blog post"""
    title = models.CharField(max_length=200)
    post_date = models.DateField()
    author = models.ForeignKey(Blogger, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, help_text="Enter the text of the blog post")

    def __str__(self):
        """String for representing the Model object"""
        return f'{self.title} - {self.author}'

    def get_absolute_url(self):
        """Returns the url to access a particular blogpost instance"""
        return reverse('blogpost-detail', args=[str(self.id)])


class Comment(models.Model):
    blogpost = models.ForeignKey(BlogPost, on_delete=models.SET_NULL, null=True)
    post_time = models.DateTimeField()
    commenter = models.CharField(max_length=100, help_text="Enter your name")
    text = models.TextField(max_length=1000, help_text="Enter your comment")

    def __str__(self):
        """String for representing the Model object"""
        return self.text[:75]
