# Generated by Django 5.0.6 on 2024-06-10 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("online_shop_app", "0002_alter_product_created_at_alter_product_updated_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Имя")),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Телефон"
                    ),
                ),
                (
                    "message",
                    models.TextField(blank=True, null=True, verbose_name="Сообщение"),
                ),
            ],
            options={
                "verbose_name": "Контакт",
                "verbose_name_plural": "Контакты",
            },
        ),
    ]
