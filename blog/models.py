from django.db import models
from django.urls import reverse

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    blogger = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    post_date = models.DateField(auto_now_add=True)
    text = models.TextField(help_text='Enter a text of blog')

    class Meta():
        ordering = ['-post_date', 'id']

    def __str__(self):
        return '{0}: {1}'.format(self.id, self.name)

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])


class Blogger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        # permissions = (('can_create_blogers', 'Can create, update and delete blogers'),)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('blogger-detail', args=[str(self.id)])
    

class Comment(models.Model):
    post_date = models.DateTimeField(auto_now_add=True)
    blogger = models.ForeignKey('Blogger', on_delete=models.CASCADE)
    blog = models.ManyToManyField('Blog')
    text = models.CharField(max_length=1000)

    class Meta:
        ordering = ['-post_date', 'id']

    def __str__(self):
        return '{0} {1}: {2}'.format(self.id, self.post_date, self.text[:20])

    
    
    
