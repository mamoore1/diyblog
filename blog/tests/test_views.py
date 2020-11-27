import datetime

from django.test import TestCase
from django.urls import reverse

from blog.models import Blogger, BlogPost

class BloggerListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 8 bloggers for pagination tests
        number_of_bloggers = 8

        for blogger_id in range(number_of_bloggers):
            Blogger.objects.create(username=f'username {blogger_id}',
                                   bio=f"Hello, I'm Blogger {blogger_id}",
                                   )

    def test_view_url_exists_at_desired_loction(self):
        response = self.client.get('/blog/bloggers/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('bloggers'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bloggers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogger_list.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('bloggers'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['blogger_list']) == 5)

    def test_lists_all_bloggers(self):
        # Get second page and confirm it has (exactly) remaining 3 times
        response = self.client.get(reverse('bloggers')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['blogger_list']) == 3)

class BlogPostListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a blogger for pagination tests
        Blogger.objects.create(username=f'username', bio=f"Hello, I'm a Blogger")

        # Create 8 blog posts to test pagination
        number_of_blogposts = 8
        for blogpost_id in range(number_of_blogposts):
            BlogPost.objects.create(title=f"Title {blogpost_id}",
                                   post_date=datetime.datetime.now(),
                                   author=Blogger.objects.get(id=1),
                                   description=f"Blog contents for post {blogpost_id}"
                                   )

    def test_view_url_exists_at_desired_loction(self):
        response = self.client.get('/blog/blogs/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blogposts'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blogposts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogpost_list.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('blogposts'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['blogpost_list']) == 5)

    def test_lists_all_bloggers(self):
        # Get second page and confirm it has (exactly) remaining 3 times
        response = self.client.get(reverse('blogposts')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['blogpost_list']) == 3)
