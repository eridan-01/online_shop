from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from django.views.generic.base import TemplateView

from online_shop_app.froms import ProductForm, VersionForm
from online_shop_app.models import Contact, Version

from online_shop_app.models import Product


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        list_product = Product.objects.all().prefetch_related('versions')

        for product in list_product:
            active_version = product.versions.filter(is_active=True).last()
            if active_version:
                product.active_version = active_version.name_version
                product.number_version = active_version.number_version
            else:
                product.active_version = 'Нет активной версии'

        context_data['object_list'] = list_product
        return context_data


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


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('online_shop_app:product_list')


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('online_shop_app:product_list')
