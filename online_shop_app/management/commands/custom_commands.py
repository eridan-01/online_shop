from django.core.management.base import BaseCommand
from online_shop_app.models import Category, Product
import json


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('category.json') as f:
            categories_data = json.load(f)
        return categories_data

    @staticmethod
    def json_read_products():
        with open('product.json') as f:
            products_data = json.load(f)
        return products_data

    def handle(self, *args, **options):
        # Удаляем все продукты и категории
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создаем категории
        category_for_create = []
        for category_data in Command.json_read_categories():
            category_for_create.append(
                Category(
                    name_of_category=category_data['fields']['name_of_category'],
                    description=category_data['fields']['description']
                )
            )
        Category.objects.bulk_create(category_for_create)

        # Создаем продукты
        product_for_create = []
        for product_data in Command.json_read_products():
            product_for_create.append(
                Product(
                    name=product_data['fields']['name'],
                    description=product_data['fields']['description'],
                    preview=product_data['fields']['preview'],
                    price=product_data['fields']['price']
                )
            )
        Product.objects.bulk_create(product_for_create)

        self.stdout.write(self.style.SUCCESS('Successfully imported categories and online_shop_app.'))
