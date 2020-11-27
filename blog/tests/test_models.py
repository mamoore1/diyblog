import datetime

from django.test import TestCase

from blog.models import Blogger, BlogPost, Comment


class BloggerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Blogger.objects.create(username="Big Ben", bio="A blogger for the website, who sure writes a lot of blogposts")

    def test_username_label(self):
        blogger =  Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('username').verbose_name
        self.assertEqual(field_label, 'username')

    def test_bio_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('bio').verbose_name
        self.assertEqual(field_label, 'bio')

    def test_username_max_length(self):
        blogger = Blogger.objects.get(id=1)
        max_length = blogger._meta.get_field('username').max_length
        self.assertEqual(max_length, 100)

    def test_bio_max_length(self):
        blogger = Blogger.objects.get(id=1)
        max_length = blogger._meta.get_field('bio').max_length
        self.assertEqual(max_length, 1000)

    def test_bio_help_text(self):
        blogger = Blogger.objects.get(id=1)
        label_text = blogger._meta.get_field('bio').help_text
        self.assertEqual(label_text, 'Enter a brief description of the blogger')

    def test_object_name_is_username(self):
        blogger = Blogger.objects.get(id=1)
        expected_object_name = blogger.username
        self.assertEqual(expected_object_name, str(blogger))
        
    def test_get_absolute_url(self):
        blogger = Blogger.objects.get(id=1)
        self.assertEqual(blogger.get_absolute_url(), '/blog/bloggers/1')


class BlogPostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a Blogger
        Blogger.objects.create(username="Big Ben", bio="A blogger for the website, who sure writes a lot of blogposts")
        # Create a Blog Post
        BlogPost.objects.create(title="Hello, world!", post_date=datetime.datetime.now(), author=Blogger.objects.get(id=1), description="Hello everybody in the world")

    def test_title_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')
    
    def test_post_data_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field('post_date').verbose_name
        self.assertEqual(field_label, 'post date')
        
    def test_author_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')
        
    def test_description_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_title_max_length(self):
        blogpost = BlogPost.objects.get(id=1)
        max_length = blogpost._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_description_max_length(self):
        blogpost = BlogPost.objects.get(id=1)
        max_length = blogpost._meta.get_field('description').max_length
        self.assertEqual(max_length, 1000)

    def test_description_help_text(self):
        blogpost = BlogPost.objects.get(id=1)
        label_text = blogpost._meta.get_field('description').help_text
        self.assertEqual(label_text, 'Enter the text of the blog post')

    def test_object_name_is_title_and_author(self):
        blogpost = BlogPost.objects.get(id=1)
        expected_object_name = f'{blogpost.title} - {blogpost.author}'
        self.assertEqual(expected_object_name, str(blogpost))

    def test_get_absolute_url(self):
        blogpost = BlogPost.objects.get(id=1)
        self.assertEqual(blogpost.get_absolute_url(), '/blog/blogs/1')


class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a Blogger
        Blogger.objects.create(username="Big Ben", bio="A blogger for the website, who sure writes a lot of blogposts")
        # Create a BlogPost
        BlogPost.objects.create(title="Hello, world!", post_date=datetime.datetime.now(), author=Blogger.objects.get(id=1),
                                description="Hello everybody in the world")
        # Create a Comment
        Comment.objects.create(blogpost=BlogPost.objects.get(id=1), post_time=datetime.datetime.now(), commenter='Alex',
                               text='What a terrible post')

    def test_blogpost_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('blogpost').verbose_name
        self.assertEqual(field_label, 'blogpost')

    def test_post_time_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('post_time').verbose_name
        self.assertEqual(field_label, 'post time')

    def test_commenter_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('commenter').verbose_name
        self.assertEqual(field_label, 'commenter')

    def test_text_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('text').verbose_name
        self.assertEqual(field_label, 'text')

    def test_commenter_max_length(self):
        comment = Comment.objects.get(id=1)
        max_length = comment._meta.get_field('commenter').max_length
        self.assertEqual(max_length, 100)

    def test_text_max_length(self):
        comment = Comment.objects.get(id=1)
        max_length = comment._meta.get_field('text').max_length
        self.assertEqual(max_length, 1000)

    def test_commenter_help_text(self):
        comment = Comment.objects.get(id=1)
        label_text = comment._meta.get_field('commenter').help_text
        self.assertEqual(label_text, 'Enter your name')

    def test_text_help_text(self):
        comment = Comment.objects.get(id=1)
        label_text = comment._meta.get_field('text').help_text
        self.assertEqual(label_text, 'Enter your comment')

    def test_object_name_is_title_and_author(self):
        comment = Comment.objects.get(id=1)
        expected_object_name = comment.text[:75]
        self.assertEqual(expected_object_name, str(comment))


