from django.urls import path
from core import views

app_name="core"
urlpatterns=[
    # common
    path("",views.HomeView.as_view(),name="home"),
    path("about/",views.AboutView.as_view(),name="about_us"),
    path("action/",views.ActionView.as_view(),name="choose_action"),
    # feedback
    path("feedback_create/",views.FeedbackCreateView.as_view(),name="feedback_create"),
    path("feedback_list/",views.FeedbackListView.as_view(),name="feedback_list"),
    # product
    path("view_list/",views.ProductListView.as_view(),name="product_list"),
    path("product_purchase/",views.ProductPurchaseView.as_view(),name="product_purchase"),
    # category
    path("category_list/",views.CategoryListView.as_view(),name="category_list"),
    # product by card
    path("product_by_card_category/<int:pk>/list",views.ProductByCardCategoryView.as_view(),name="product_by_card_category"),
    # delivery
    path("product_delivery/",views.ProductDeliveryView.as_view(),name="product_delivery"),
    # add new address
    path("add_address/",views.AddAddressView.as_view(),name="add_address"),
    # product summary
    path("product_summary/",views.ProductSummaryView.as_view(),name="product_summary"),
    # payment
    path("payment/",views.PaymentView.as_view(),name="payment"),
    # success
    path("success/",views.SuccessView.as_view(),name="success"),
]