# Generated by Django 4.1.2 on 2022-11-10 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_productmodel_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="cardcategorymodel",
            name="subject",
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]