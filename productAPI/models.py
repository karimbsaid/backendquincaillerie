from django.db import models

# Create your models here.
class ProductList(models.Model):
      name= models.CharField(max_length=255)
      category= models.CharField(max_length=255)
      price=models.DecimalField(max_digits=10 , decimal_places=5)
      reference = models.CharField(max_length=255) 
      photo = models.ImageField(upload_to='products/', null=True, blank=True)

      
# "name": "Ignition Coil",
#       "category": "Electrical",
#       "price": 55.99,
#       "description": "High-performance ignition coil for reliable ignition system performance.",
#       "reference": "CAR-ELEC-006",
#       "photo": "https://tailwindui.com/img/ecommerce-images/product-page-01-related-product-01.jpg"