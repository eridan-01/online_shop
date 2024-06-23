from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from django.views.generic.base import TemplateView

from online_shop_app.froms import ProductForm
from online_shop_app.models import Contact

from online_shop_app.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    # fields = ('name', 'description', 'preview', 'category', 'price')
    form_class = ProductForm
    success_url = reverse_lazy('online_shop_app:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    # fields = ('name', 'description', 'preview', 'category', 'price')
    form_class = ProductForm
    success_url = reverse_lazy('online_shop_app:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('online_shop_app:product_list')


class ContactView(TemplateView):
    template_name = "online_shop_app/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_contacts"] = Contact.objects.all()[:5]
        return context
