from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import BlogArticle


class BlogArticleListView(ListView):
    model = BlogArticle


class BlogArticleDetailView(DetailView):
    model = BlogArticle


class BlogArticleCreateView(CreateView):
    model = BlogArticle
    fields = ('title', 'text', 'preview')



class BlogArticleUpdateView(UpdateView):
    model = BlogArticle


class BlogArticleDeleteView(DeleteView):
    model = BlogArticle


