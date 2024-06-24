# Generated by Django 5.0.6 on 2024-06-24 11:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("online_shop_app", "0003_contact"),
    ]

    operations = [
        migrations.CreateModel(
            name="Version",
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
                (
                    "number_version",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="Номер версии"
                    ),
                ),
                (
                    "name_version",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Название версии",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=False, verbose_name="Активна"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="versions",
                        to="online_shop_app.product",
                        verbose_name="Продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Версия",
                "verbose_name_plural": "Версии",
                "ordering": ["number_version"],
            },
        ),
    ]