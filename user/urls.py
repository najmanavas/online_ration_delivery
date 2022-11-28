from django.urls import path

from core import views
from user import views


app_name = "user"

urlpatterns = [
    path("sign_up/", views.UserCreateView.as_view(), name = "user_signup"),
    path("login/", views.UserLoginView.as_view(), name = "user_login"),
    path("logged_out/",views.UserLogoutView.as_view(),name="user_logout"),
    # card details
    path("card_details/",views.CardDetailView.as_view(),name="card_details"),
    # profile
    path("profile/create/", views.ProfileCreateView.as_view(), name="profile_create"),
    path("profile/<int:pk>/detail/", views.ProfileDetailView.as_view(), name="profile_detail"),
    path("profile/<int:pk>/update/",views.ProfileUpdateView.as_view(),name="profile_update"), 
    # address
    path("add_address/",views.AddressCreateView.as_view(),name="add_address"),
    path("address/<int:pk>/update/",views.AddressUpdateView.as_view(),name="address_update"),
    path("product_delivery/",views.DeliveryDetailView.as_view(),name="product_delivery"),
]
