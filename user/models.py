from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from core import models as core_models
from django.urls import reverse

USER = settings.AUTH_USER_MODEL
class CustomUser(AbstractUser):
    pass

class LocationModel(models.Model):
    lattitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.lattitude},{self.longitude}"
class AddressModel(models.Model):
    name=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=15)
    building_name = models.CharField(max_length=64)
    place = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    district = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    country = models.CharField(max_length=24, default="India")
    postal_code = models.CharField(max_length=6)
    location = models.ForeignKey(
        LocationModel, on_delete=models.SET_NULL, null=True, blank=True
    )
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.building_name},{self.place}-{self.postal_code}"


class ProfileModel(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Others"),
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to="user/profile/image/", default="default/user.png")
    phone_number = models.CharField(max_length=15)
    card_type=models.ManyToManyField(core_models.CardModel, blank=True)
    email=models.EmailField(max_length=100)
    address = models.ManyToManyField(AddressModel, blank=True)
    user = models.OneToOneField(USER, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}".title()

    def get_absolute_url(self):
        url=reverse("user:profile_detail",kwargs={'pk':self.id})

    