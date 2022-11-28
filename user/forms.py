from django import forms
from user import models as user_models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

USER = get_user_model()

# User Registration Form
class UserRegisterform(UserCreationForm):
    class Meta:
        model = USER
        fields = ["email", "username"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = user_models.ProfileModel
        exclude = ("status","updated_on","created_on","user","address")

class AddressForm(forms.ModelForm):
    class Meta:
        model = user_models.AddressModel
        exclude = ("status","updated_on","created_on")