from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name_of_category = models.CharField(
        max_length=100, verbose_name="Название категории"
    )
    description = models.TextField(verbose_name="Описание", **NULLABLE)

    def __str__(self):
        return f"{self.name_of_category}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", **NULLABLE)
    preview = models.ImageField(
        upload_to="online_shop_app/products",
        verbose_name="Изображение (превью)",
        **NULLABLE,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория товара",
        **NULLABLE,
        related_name="products",
    )
    price = models.IntegerField()
    created_at = models.DateTimeField(
        blank=True, verbose_name="Дата создания (записи в БД)"
    )
    updated_at = models.DateTimeField(
        blank=True, verbose_name="Дата последнего изменения (записи в БД)"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

