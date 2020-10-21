from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User
from blog.models import Blog, Blogger, BlogComment


class BlogListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create User
        user = User.objects.create_user(username='Heal123', password='NJ#NKsd!!3492')
        user.save()
        # Create Blogger
        blogger = Blogger.objects.create(user=user)
        # Create 3 blogs for pagination tests
        number_of_blogs = 3
        text_template = "Test text "
        name_template = "Test name "
        
        for blog_id in range(number_of_blogs): 
            text = text_template + str(blog_id)
            name = name_template + str(blog_id)
            Blog.objects.create(blogger=blogger, name=name, text=text)
           
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('blogs'))
        self.assertRedirects(response, '/accounts/login/?next=/blog/blogs/')
        
    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(username='Heal123', password='NJ#NKsd!!3492')
        response = self.client.get('/blog/blogs/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        login = self.client.login(username='Heal123', password='NJ#NKsd!!3492')
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        login = self.client.login(username='Heal123', password='NJ#NKsd!!3492')
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_list.html')
        
    def test_pagination_is_two(self):
        login = self.client.login(username='Heal123', password='NJ#NKsd!!3492')
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['blog_list']) == 2)

    def test_lists_all_blogs(self):
        # Get second page and confirm it has (exactly) remaining 1 item
        login = self.client.login(username='Heal123', password='NJ#NKsd!!3492')
        response = self.client.get(reverse('blogs')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['blog_list']) == 1)


class BlogDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create Users
        user1 = User.objects.create_user(username='User1', password='NJ#NKsd!!3492')
        user1.save()
        user2 = User.objects.create_user(username='User2', password='Nu&8%&^872j')
        user2.save()
        user3 = User.objects.create_user(username='User3', password='nkjUYI^5657HJb')
        user3.save()
        # Create Blogger
        blogger = Blogger.objects.create(user=user1)
        
        # Create 2 blogs
        number_of_blogs = 2
        text_template = "Test text "
        name_template = "Test name "
        
        for blog_id in range(number_of_blogs): 
            text = text_template + str(blog_id)
            name = name_template + str(blog_id)
            Blog.objects.create(blogger=blogger, name=name, text=text)
        
        # Create comments. Each blog has to have 3 comments with different authors
        users = (user1, user2, user3)
        blogs = Blog.objects.all()
        
        for blog in blogs:
            for user in users:
                text = ' - '.join((user.__str__(), blog.__str__()))
                BlogComment.objects.create(author=user, blog=blog, text=text)
               
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('blog-detail', kwargs={'pk': 1,}))
        self.assertRedirects(response, '/accounts/login/?next=/blog/blog/1/')
        response = self.client.get(reverse('blog-detail', kwargs={'pk': 2,}))
        self.assertRedirects(response, '/accounts/login/?next=/blog/blog/2/')
        
    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(username='User1', password='NJ#NKsd!!3492')
        response = self.client.get('/blog/blog/1/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        login = self.client.login(username='User1', password='NJ#NKsd!!3492')
        response = self.client.get(reverse('blog-detail', kwargs={'pk': 1,}))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        login = self.client.login(username='User1', password='NJ#NKsd!!3492')
        response = self.client.get(reverse('blog-detail', kwargs={'pk': 1,}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_detail.html')
        
    def test_view_has_all_its_comments_by_blogger(self):
        login = self.client.login(username='User1', password='NJ#NKsd!!3492')
        response = self.client.get(reverse('blog-detail', kwargs={'pk': 1,}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['comments'].count(), 3)
        
        