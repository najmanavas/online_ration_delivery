from django.db import models
from django.conf import settings

USER = settings.AUTH_USER_MODEL


class TimeStamp(models.Model):
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# feedback model
class FeedbackModel(TimeStamp, models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name}"


# unit model
class UnitModel(TimeStamp, models.Model):
    name = models.CharField(max_length=64)
    symbol = models.CharField(max_length=8)
    convertion_rate = models.FloatField()
    secondary = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.name}"


# product category model
class CategoryModel(TimeStamp, models.Model):
    name = models.CharField(max_length=64)
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name}"


# product model
class ProductModel(TimeStamp, models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField(max_length=100)
    unit = models.ForeignKey(
        UnitModel, on_delete=models.SET_NULL, null=True, blank=True
    )
    category = models.ManyToManyField(CategoryModel)
    image = models.ImageField(
        upload_to="product/image",
        default="default/product.png",
    )

    def __str__(self):
        return f"{self.name}"


# category of cards
class CardModel(TimeStamp, models.Model):
    class CardTypeChoice(models.TextChoices):
        APL = "apl", "APL"
        BPL = "bpl", "BPL"
        AAY = "aay", "AAY"
        NPNS = "npns", "NPNS"

    name = models.CharField(max_length=64)
    description = models.TextField(max_length=500)
    type = models.CharField(max_length=5, choices=CardTypeChoice.choices)

    def __str__(self):
        return f"{self.name}({self.CardTypeChoice(self.type).name})"


# stock model
class StockModel(TimeStamp, models.Model):
    card = models.ForeignKey(CardModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.product}(Qty - {self.quantity})"


class QuotaModel(TimeStamp, models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    stock = models.ForeignKey(StockModel, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        name = f"{self.stock} is not available for {self.user}"
        if self.is_available:
            name = f"{self.stock} is available for {self.user}"
        return name


#  cart
class CartModel(TimeStamp, models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    checked_out = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}"

    def items(self):
        cart_items = CartItemModel.objects.filter(cart=self, status=True)
        return cart_items


# cart item model
class CartItemModel(TimeStamp, models.Model):
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return f"{self.product}({self.quantity})"
