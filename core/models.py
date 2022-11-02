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

# product model
class ProductModel(models.Model):
    name=models.CharField(max_length=64)
    price=models.FloatField(max_length=100)
    quantity=models.FloatField(max_length=100)
    image=models.ImageField(upload_to="product/image",default="default/product.png")
    status=models.BooleanField(default=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name}"
