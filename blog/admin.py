from django.contrib import admin
from .models import Blogger, BlogPost, Comment

# Register your models here.
# admin.site.register(Blogger)
# admin.site.register(BlogPost)
admin.site.register(Comment)


# Define the blog post inline class
class BlogPostInLine(admin.TabularInline):
    model = BlogPost
    extra = 0


# Define the comment inline class
class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0


# Define the Blogger admin class
@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('username', 'bio')
    inlines = [BlogPostInLine]


# Define the BlogPost admin class
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'post_date')
    inlines = [CommentInLine]
