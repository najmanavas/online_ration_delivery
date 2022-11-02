from django import forms
from core import models

# for feedback
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.FeedbackModel
        exclude = ("status",)

# for product
class ProductForm(forms.ModelForm):
    class Meta:
        model=models.ProductModel
        exclude=("status","updated_on","created_on")