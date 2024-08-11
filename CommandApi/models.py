from django.db import models
from django.contrib.auth.models import User
from productAPI.models import ProductList  # Assuming your product model is in ProductApi

# Create your models here.
class Command(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(ProductList, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} - {self.quantity}"