# Generated by Django 5.1.1 on 2024-11-28 13:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_product_options_product_is_published"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "category", "created_at"],
                "permissions": [
                    ("can_unpublish_product", "Can Unpublish Product"),
                    ("only_owners", "Только Владельцы"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="owner",
            field=models.ForeignKey(
                default=1,
                max_length=200,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Product",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
            preserve_default=False,
        ),
    ]