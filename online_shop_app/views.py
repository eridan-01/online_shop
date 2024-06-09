from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from online_shop_app.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'preview', 'category', 'price')
    success_url = reverse_lazy('online_shop_app:product_list')


def contacts(request):
    return render(request, 'online_shop_app/contacts.html')

