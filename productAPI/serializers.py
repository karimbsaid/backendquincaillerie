from rest_framework import serializers
from .models import ProductList
class ProductListeSerializers(serializers.ModelSerializer):
    class Meta :
        model=ProductList
        fields = '__all__'