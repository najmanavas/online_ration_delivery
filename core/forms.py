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
        model = models.ProductModel
        exclude = ("status", "updated_on", "created_on")


class ProductPurchaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        card_id = kwargs.pop("card")
        super().__init__(*args, **kwargs)
        queryset = models.ProductModel.objects.filter(stockmodel__card__id=card_id)
        self.fields.update(
            {
                "products": forms.ModelMultipleChoiceField(queryset=queryset),
            }
        )
