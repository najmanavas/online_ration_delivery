from django.shortcuts import redirect
from django.views import generic as views
from core import models as core_models
from core.forms import FeedbackForm, ProductForm
from django.urls import reverse_lazy
from django.contrib import messages

# home view
class HomeView(views.TemplateView):
    template_name="core/home.html"
    extra_context={}

# about_us view
class AboutView(views.TemplateView):
    template_name="core/about_us.html"


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

# # ------------for cart------------
# class AddToCartView(views.View):
#     def get(self,request,pk):
#         user=request.user
#         product=core_models.ProductModel.objects.get(id=pk)
#         cart, cart_created = core_models.CartModel.objects.get_or_create(
#             user=user, checked_out=False
#         )
#         cart_item, cart_item_created = core_models.CartItemModel.objects.get_or_create(
#             cart=cart, product=product
#         )
#         if not cart_item_created:
#             cart_item.quantity +=1
#         cart_item.save()
#         messages.success(request,"PRODUCT ADDED SUCCESSFULLY ..!")
#         url=request.META.get("HTTP_REFERER")
#         return redirect(url)

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

# choose actions view
class ActionView(views.TemplateView):
    template_name="core/actions.html"
    extra_context={"products":core_models.ProductModel.objects.all()}

# view card details
class CardDetailView(views.TemplateView):
    template_name="core/card_details.html"

# profile
class ProfileView(views.TemplateView):
    template_name="user/profile.html"
# add details
class AboutMeView(views.TemplateView):
    template_name="user/about_me.html"

# payment
class PaymentView(views.TemplateView):
    template_name="core/payment.html"