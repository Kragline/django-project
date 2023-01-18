from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import  ListView ,DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


class PostListView(ListView):
    model = Post
    template_name = 'mainapp/index.html' 

    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(PostListView, self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context


class PostDetailsView(DetailView):
    model = Post
    template_name = 'mainapp/details.html'

    def get_context_data(self,*args,**kwargs):
        context = super(PostDetailsView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context['total_likes'] = total_likes
        cat_menu = Category.objects.all()
        context["cat_menu"] = cat_menu
        return context


def LikeWiew(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('like-post'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('detailview', args=[str(pk)]))
    

def CategoryView(request, cats):    
    # category is the "category" field in Post model in models.py
    category_posts = Post.objects.filter(category = cats)
    return render(request, 'mainapp/categories.html', {'category_posts' : category_posts, 'cats' : cats})


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'mainapp/add.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'mainapp/update.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'mainapp/delete.html'
    success_url = reverse_lazy('home')


    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def search_posts(request):
    if request.method == "POST":
        searched = request.POST[('searched')]
        results = Post.objects.filter(content__contains=searched)

        return render(request, 'mainapp/search.html', {'searched' : searched, 'results' : results})
    else:
        return render(request, 'mainapp/search.html', {})