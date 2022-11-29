from django.db import models

# feedback model
class FeedbackModel(models.Model):
    name=models.CharField(max_length=64)
    email=models.EmailField()
    subject=models.CharField(max_length=120)
    message=models.TextField(max_length=500)
    status=models.BooleanField(default=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name}"

# unit model
class UnitModel(models.Model):
    name=models.CharField(max_length=64)
    symbol=models.CharField(max_length=8)
    convertion_rate=models.FloatField()
    secondary=models.ForeignKey("self",on_delete=models.SET_NULL,null=True,blank=True)
    status=models.BooleanField(default=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name}"

# product category model
class CategoryModel(models.Model):
    name=models.CharField(max_length=64)
    parent=models.ForeignKey("self",on_delete=models.SET_NULL,null=True,blank=True)
    status=models.BooleanField(default=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name}"

# stock model
class StockModel(models.Model):
    quantity=models.FloatField(max_length=100)
    def __str__(self):
        return f"{self.quantity}"

# product model
class ProductModel(models.Model):
    name=models.CharField(max_length=64)
    price=models.FloatField(max_length=100)
    unit=models.CharField(max_length=5)
    category=models.ManyToManyField(CategoryModel)
    image=models.ImageField(upload_to="product/image",default="default/product.png")
    status=models.BooleanField(default=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name}"


# category of cards
class CardModel(models.Model):
    name=models.CharField(max_length=64)
    subject=models.CharField(max_length=500)
    product=models.ManyToManyField(ProductModel)
    quantity=models.ManyToManyField(StockModel)
    status=models.BooleanField(default=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name}"


# #  cart
# class CartModel(models.Model):
#     user=models.ForeignKey(USER,on_delete=models.CASCADE)
#     checked_out=models.BooleanField(default=False)
#     status=models.BooleanField(default=True)
#     created_on=models.DateTimeField(auto_now_add=True)
#     updated_on=models.DateTimeField(auto_now=True)

#     def items(self):
#         cart_items=CartItemModel.objects.filter(
#             cart=self,
#             status=True
#         )
#         return cart_items
#     def __str__(self):
#         return f"{self.user}"

# # cart item model
# class CartItemModel(models.Model):
#     cart=models.ForeignKey(CartModel,on_delete=models.CASCADE)
#     product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
#     quantity=models.PositiveIntegerField(default=1)
#     status=models.BooleanField(default=True)
#     created_on=models.DateTimeField(auto_now_add=True)
#     updated_on=models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.product}({self.quantity})"
