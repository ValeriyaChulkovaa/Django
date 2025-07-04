# Generated by Django 5.1.1 on 2024-10-23 21:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "name",
                    models.CharField(help_text="Введите наименование", max_length=100, verbose_name="Наименование"),
                ),
                (
                    "description",
                    models.TextField(blank=True, help_text="Введите описание", null=True, verbose_name="Описание"),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "name",
                    models.CharField(help_text="Введите наименование", max_length=100, verbose_name="Наименование"),
                ),
                (
                    "description",
                    models.TextField(blank=True, help_text="Введите описание", null=True, verbose_name="Описание"),
                ),
                (
                    "images",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фото",
                        null=True,
                        upload_to="catalog/photo",
                        verbose_name="Фото",
                    ),
                ),
                ("purchase_price", models.IntegerField(help_text="Введите цену", verbose_name="Цена")),
                ("created_at", models.DateField(auto_now_add=True, verbose_name="Дата создания")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")),
                (
                    "category",
                    models.ForeignKey(
                        help_text="Выберите категорию",
                        max_length=100,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["name", "category", "created_at"],
            },
        ),
    ]