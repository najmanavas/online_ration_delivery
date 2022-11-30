# Generated by Django 4.1.2 on 2022-11-30 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_productmodel_unit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stockmodel",
            name="product",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="core.productmodel"
            ),
        ),
    ]