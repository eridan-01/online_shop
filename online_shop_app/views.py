from django.shortcuts import render, get_object_or_404

from online_shop_app.models import Product


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products_list.html', context)


def contacts(request):
    return render(request, 'contacts.html')


def products_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'products_detail.html', context)
