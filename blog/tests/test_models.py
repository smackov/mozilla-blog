from django.test import TestCase

from django.contrib.auth.models import User
from blog.models import Blog, Blogger, BlogComment


class BlogModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='Heal123', password='NJ#NKsd!!3492')
        user.save()
        blogger = Blogger.objects.create(user=user)
        text = """
            Returns the object matching the given lookup parameters, which should be in the format described in Field lookups. 
            You should use lookups that are guaranteed unique, such as the primary key or fields in a unique constraint. For example:
        """
        name = "My love - my pets"
        Blog.objects.create(blogger=blogger, name=name, text=text)

    def test_name_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_help_text_of_text_field(self):
        blog = Blog.objects.get(id=1)
        help_text = blog._meta.get_field('text').help_text
        self.assertEquals(help_text, 'Enter a text of blog')

    def test_get_absolute_url(self):
        blog = Blog.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(blog.get_absolute_url(), '/blog/blog/1/')
        
    def test_object_name(self):
        blog = Blog.objects.get(id=1)
        expected_object_name = '{0}: {1}'.format(blog.id, blog.name)
        self.assertEquals(expected_object_name, str(blog))


class BloggerModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='Heal123', password='NJ#NKsd!!3492')
        user.save()
        blogger = Blogger.objects.create(user=user)
        
    def test_date_of_death_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'Died')

    def test_date_of_born_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label, 'date of birth')

    def test_user_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('user').verbose_name
        self.assertEquals(field_label, 'user')

    def test_get_absolute_url(self):
        blogger = Blogger.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(blogger.get_absolute_url(), '/blog/blogger/1/')
        
    def test_object_name(self):
        blogger = Blogger.objects.get(id=1)
        expected_object_name = blogger.user.username
        self.assertEquals(expected_object_name, str(blogger))


class BlogCommentModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        user_1 = User.objects.create_user(username='Heal123', password='NJ#NKsd!!3492')
        user_1.save()
        user_2 = User.objects.create_user(username='Ipgnaee', password='34gvreJKHk#*&@#jkdfn')
        user_2.save()
        blogger = Blogger.objects.create(user=user_1)
        text = """
            Returns the object matching the given lookup parameters, which should be in the format described in Field lookups. 
            You should use lookups that are guaranteed unique, such as the primary key or fields in a unique constraint. For example:
        """
        name = "My love - my pets"
        blog = Blog.objects.create(blogger=blogger, name=name, text=text)
        text_of_comment = "Great. This is a good idea =)"
        BlogComment.objects.create(author=user_2, blog=blog, text=text_of_comment)
        
    def test_text_label(self):
        comment = BlogComment.objects.get(id=1)
        field_label = comment._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'text')
        
    def test_blog_label(self):
        comment = BlogComment.objects.get(id=1)
        field_label = comment._meta.get_field('blog').verbose_name
        self.assertEquals(field_label, 'blog')

    def test_text_max_length(self):
        comment = BlogComment.objects.get(id=1)
        max_length = comment._meta.get_field('text').max_length
        self.assertEquals(max_length, 1000)
        
    def test_object_name(self):
        comment = BlogComment.objects.get(id=1)
        
        len_title = 30
        if len(comment.text) > len_title:
            title = comment.text[:len_title] + '...'
        else:
            title = comment.text
            
        expected_object_name = '{0} {1}: {2}'.format(comment.id, comment.post_date, title)
        self.assertEquals(expected_object_name, str(comment))
    