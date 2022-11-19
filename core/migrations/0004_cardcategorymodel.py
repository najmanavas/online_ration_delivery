# Generated by Django 4.1.2 on 2022-11-09 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_productmodel_unit"),
    ]

    operations = [
        migrations.CreateModel(
            name="CardCategoryModel",
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
                ("name", models.CharField(max_length=64)),
                ("status", models.BooleanField(default=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
