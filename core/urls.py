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
    path("card_list/",views.CardListView.as_view(),name="card_list"),
    # product by card
    path("product_by_card/<int:pk>/list",views.ProductByCardView.as_view(),name="product_by_card"),
    # product summary
    path("product_summary/",views.ProductSummaryView.as_view(),name="product_summary"),
    # payment
    path("payment/",views.PaymentView.as_view(),name="payment"),
    # success
    path("success/",views.SuccessView.as_view(),name="success"),
]