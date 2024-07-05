from django.db import models

from users.models import User

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
        **NULLABLE, verbose_name="Дата создания (записи в БД)"
    )
    updated_at = models.DateTimeField(
        **NULLABLE, verbose_name="Дата последнего изменения (записи в БД)"
    )
    owner = models.ForeignKey(
        User,
        verbose_name='Проектировщик',
        help_text='Укажите проектировщика',
        **NULLABLE,
        on_delete=models.SET_NULL
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        permissions = [
            ('can_change_is_published', 'Can change sign of publication'),
            ('can_edit_description', 'Can edit description'),
            ('can_edit_category', 'Can edit category')
        ]


class Contact(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Имя",
    )
    phone = models.CharField(
        max_length=50,
        verbose_name="Телефон",
        null=True,
        blank=True,
    )
    message = models.TextField(
        verbose_name="Сообщение",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions', verbose_name='Продукт')
    number_version = models.PositiveIntegerField(verbose_name='Номер версии', **NULLABLE)
    name_version = models.CharField(max_length=100, verbose_name='Название версии', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='Активна')

    def __str__(self):
        return self.name_version

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ['number_version']
