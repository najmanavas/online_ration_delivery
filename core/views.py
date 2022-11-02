from django.shortcuts import render
from django.views import generic as views
from core import models as core_models
from core.forms import FeedbackForm, ProductForm
from django.urls import reverse_lazy

# home view
class HomeView(views.TemplateView):
    template_name="core/home.html"
    extra_context={}

# about_us view
class AboutView(views.TemplateView):
    template_name="core/about_us.html"

# choose actions view
class ActionView(views.TemplateView):
    template_name="core/actions.html"
    extra_context={"products":core_models.ProductModel.objects.all()}

# view product list
class ProductListView(views.ListView):
    template_name="product/view_list.html"
    model=core_models.ProductModel
    form_class=ProductForm

# view product purchase
class ProductPurchaseView(views.TemplateView):
    template_name="product/purchase.html"
    model=core_models.ProductModel
    form_class=ProductForm

# address adding
class AddAddressView(views.TemplateView):
    template_name="delivery/new_address.html"

# product delivery
class ProductDeliveryView(views.TemplateView):
    template_name="delivery/delivery.html"

# product summary
class ProductSummaryView(views.TemplateView):
    template_name="core/summary.html"
    
# feedback create
class FeedbackCreateView(views.CreateView):
    template_name="feedback/feedback_create.html"
    model=core_models.FeedbackModel
    form_class=FeedbackForm
    success_url=reverse_lazy("core:home")

# feedback list
class FeedbackListView(views.ListView):
    template_name="feedback/feedback_list.html"
    model=core_models.FeedbackModel
    context_object_name="feedbacks"

