from pydoc import ModuleScanner
from django.contrib import admin
from core import models

admin.site.register(models.FeedbackModel)
admin.site.register(models.UnitModel)
admin.site.register(models.ProductModel)
