from rest_framework import serializers
from  Customer.models import Customer
from inventory.models import Product
from Order.models import Order
from Cartsystem.models import Cart

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        
class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many = True)
    class Meta:
        model = Cart
        fields = "__all__"
        

        
    