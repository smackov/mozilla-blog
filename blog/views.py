from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


from .models import Blog, Blogger, BlogComment

# !Index view 
def index(request):
    
    num_bloggers = Blogger.objects.count()
    num_blogs = Blog.objects.count()
    num_comments = BlogComment.objects.count()
    
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = BlogComment.objects.filter(author=self.request.user).filter(blog=self.kwargs['pk'])
        return context
    
    
class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['name', 'text']
    
    def form_valid(self, form):
        #Add logged-in user as author of comment
        auth_user = self.request.user
        form.instance.blogger = get_object_or_404(Blogger, user=auth_user)
        # Call super-class form validation behaviour
        return super().form_valid(form)
    
    
class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ['name', 'text']
    
    
class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs')
    
 
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
    
# !Comments
class BlogCommentCreateView(CreateView, LoginRequiredMixin):
    model = BlogComment
    fields = ['text']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = Blog.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'],})
    