from django.shortcuts import render

from online_shop_app.models import Product


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products_list.html', context)


def contacts(request):
    return render(request, 'contacts.html')
