from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


from .models import Blog, Blogger, Comment

# !Index view 
def index(request):
    
    num_bloggers = Blogger.objects.count()
    num_blogs = Blog.objects.count()
    num_comments = Comment.objects.count()
    
    context = {
        'num_bloggers': num_bloggers,
        'num_blogs': num_blogs,
        'num_comments': num_comments,
    }
    
    return render(request, 'index.html', context=context)


# !Blogs view
class BlogListView(generic.ListView, LoginRequiredMixin):
    model = Blog
    paginate_by = 2
    

class BlogDetailView(generic.DetailView, LoginRequiredMixin):
    model = Blog
    
    
class BlogCreateView(PermissionRequiredMixin, CreateView):
    model = Blog
    fields = '__all__'
    # permission_required = ('catalog.can_create_blog')
    
    
class BlogUpdateView(PermissionRequiredMixin, UpdateView):
    model = Blog
    fields = '__all__'
    # permission_required = ('catalog.can_create_blog')
    
    
class BlogDeleteView(PermissionRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs')
    # permission_required = ('catalog.can_create_blog')
    
 
# !Bloggers view   
class BloggerListView(generic.ListView, LoginRequiredMixin):
    model = Blogger
    paginate_by = 2


class BloggerDetailView(generic.DetailView, LoginRequiredMixin):
    model = Blogger
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # blogger = get_object_or_404(Blogger, pk=self.kwargs['pk']) # One of ways to get necessary blogger 
        context['bloggers_blogs'] = Blog.objects.filter(blogger=self.get_object())
        return context
    
    
class BloggerCreateView(PermissionRequiredMixin, CreateView):
    model = Blogger
    fields = '__all__'
    # permission_required = ('catalog.can_create_blog')
    
    
class BloggerUpdateView(PermissionRequiredMixin, UpdateView):
    model = Blogger
    fields = '__all__'
    # permission_required = ('catalog.can_create_blog')
    
    
class BloggerDeleteView(PermissionRequiredMixin, DeleteView):
    model = Blogger
    success_url = reverse_lazy('bloggers')
    # permission_required = ('catalog.can_create_blog')
    
    