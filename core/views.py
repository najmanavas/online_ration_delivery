from django.shortcuts import redirect
from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from core import models as core_models
from core.forms import FeedbackForm, ProductForm, ProductPurchaseForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import F,Q

# ---------common-----------
# home view
class HomeView(views.TemplateView):
    template_name = "core/home.html"
    extra_context = {"cards": core_models.CardModel.objects.all()}


# about_us view
class AboutView(views.TemplateView):
    template_name = "core/about_us.html"


# choose actions view
class ActionView(views.TemplateView):
    template_name = "core/actions.html"
    extra_context = {"products": core_models.ProductModel.objects.all()}


# ----------product----------

# view pdts wrt card
class ProductByCardView(views.ListView):
    template_name = "core/actions.html"
    model = core_models.ProductModel
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        card = core_models.CardModel.objects.get(id=self.kwargs.get("pk"))
        context.update({"card": card})
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        card_pk = self.kwargs.get("pk", None)
        qs = qs.filter(stockmodel__card__id=card_pk)
        return qs


# card category list
class CardListView(views.ListView):
    template_name = "core/home.html"
    model = core_models.CardModel
    context_object_name = "categories"


# view product list
class ProductListView(views.ListView):
    template_name = "product/product_list.html"
    model = core_models.ProductModel
    form_class = ProductForm


# view product purchase
class ProductPurchaseView(LoginRequiredMixin, views.FormView):
    template_name = "product/product_purchase.html"
    model = core_models.ProductModel
    form_class = ProductPurchaseForm
    success_url = reverse_lazy("core:cart_checkout")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get("pk", None)
        products = core_models.ProductModel.objects.filter(stockmodel__card__id=pk)
        context.update({"products": products})
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        card = self.kwargs.get("pk")
        kwargs.update({"card": card})
        return kwargs
    # product added to cart
    def form_valid(self, form):
        print("#DEBUG: form data ", form.cleaned_data)
        data = form.cleaned_data
        products = data.get("products", None)
        cart, created_cart = core_models.CartModel.objects.get_or_create(
            user=self.request.user,
            checked_out=False,
        )
        for product in products:
            cart_item, created_item = core_models.CartItemModel.objects.get_or_create(
                product=product,
                cart=cart,
                quantity=product.stockmodel.quantity,
            )
        return super().form_valid(form)


# cart checkout
class CheckOutView(LoginRequiredMixin,views.View):
    template_name="product/checkout.html"
    model=core_models.CartModel




# search view
class ProductSearchView(views.ListView):
    template_name = "product/product_list.html"
    model = core_models.ProductModel
    context_object_name = "products"

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get("q", None)
        qs = qs.filter(Q(name__icontains=q) | Q(product__name__icontains=q))
        return qs


# -----------feedback-----------
# feedback create
class FeedbackCreateView(views.CreateView):
    template_name = "feedback/feedback_create.html"
    model = core_models.FeedbackModel
    form_class = FeedbackForm
    success_url = reverse_lazy("core:home")


# feedback list
class FeedbackListView(views.ListView):
    template_name = "feedback/feedback_list.html"
    model = core_models.FeedbackModel
    context_object_name = "feedbacks"


# -----------final----------
# payment
class PaymentView(views.TemplateView):
    template_name = "core/payment.html"


# product summary
class ProductSummaryView(views.TemplateView):
    template_name = "core/summary.html"


# success
class SuccessView(views.TemplateView):
    template_name = "core/success.html"
