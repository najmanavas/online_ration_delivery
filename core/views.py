from django.shortcuts import redirect
from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from core import models as core_models
from core.forms import FeedbackForm, ProductForm
from django.urls import reverse_lazy
from django.contrib import messages

# ---------common-----------
# home view
class HomeView(views.TemplateView):
    template_name="core/home.html"
    extra_context={"categories":core_models.CardCategoryModel.objects.all()}

# about_us view
class AboutView(views.TemplateView):
    template_name="core/about_us.html"

# choose actions view
class ActionView(views.TemplateView):
    template_name="core/actions.html"
    extra_context={"products":core_models.ProductModel.objects.all()}



# ----------product----------

# view pdts wrt card
class ProductByCardCategoryView(views.ListView):
    template_name="core/actions.html"
    model=core_models.ProductModel
    context_object_name="products"
    def get_queryset(self,*args,**kwargs):
        qs=super().get_queryset(*args,**kwargs)
        pk=self.kwargs.get("pk",None)
        qs=qs.filter(category__id=pk)
        return qs


# card category list
class CategoryListView(views.ListView):
    template_name="core/home.html"
    model=core_models.CardCategoryModel
    context_object_name="categories"
    

# view product list
class ProductListView(views.ListView):
    template_name="product/view_list.html"
    model=core_models.ProductModel
    form_class=ProductForm

# view product purchase
class ProductPurchaseView(views.ListView):
    template_name="product/purchase.html"
    model=core_models.ProductModel
    form_class=ProductForm
    context_object_name="products"
    # def get_queryset(self,*args,**kwargs):
    #     qs=super().get_queryset(*args,**kwargs)
    #     pk=self.kwargs.get("pk",None)
    #     qs=qs.filter(category__id=pk)
    #     return qs

    
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


# -----------feedback-----------
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


# -----------delivery----------

# address adding
class AddAddressView(views.TemplateView):
    template_name="delivery/new_address.html"

# product delivery
class ProductDeliveryView(views.TemplateView):
    template_name="delivery/delivery.html"

# -----------final----------
# payment
class PaymentView(views.TemplateView):
    template_name="core/payment.html"

# product summary
class ProductSummaryView(views.TemplateView):
    template_name="core/summary.html"
    
# success
class SuccessView(views.TemplateView):
    template_name="core/success.html"