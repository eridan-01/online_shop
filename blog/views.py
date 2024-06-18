from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import BlogArticle


class BlogArticleListView(ListView):
    model = BlogArticle

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogArticleDetailView(DetailView):
    model = BlogArticle

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogArticleCreateView(CreateView):
    model = BlogArticle
    fields = ('title', 'body', 'preview')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog_article = form.save()
            new_blog_article.slug = slugify(new_blog_article.title)
            new_blog_article.save()

        return super().form_valid(form)


class BlogArticleUpdateView(UpdateView):
    model = BlogArticle
    fields = ('title', 'body', 'preview')
    # success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog_article = form.save()
            new_blog_article.slug = slugify(new_blog_article.title)
            new_blog_article.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogArticleDeleteView(DeleteView):
    model = BlogArticle
    success_url = reverse_lazy('blog:list')
