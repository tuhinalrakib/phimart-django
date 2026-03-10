from rest_framework import serializers
from decimal import Decimal
from product.models import Category,Product, Review
from django.conf import settings
from django.contrib.auth import get_user_model

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id","name","description","product_count"]
        
    product_count = serializers.IntegerField(read_only=True)

    
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = "__all__"
        fields = ["id","name", "description","price","price_with_tax", "stock","created_at", "category"]
    
    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")
    
    """Field Lavel Validation"""
    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError("Price cound not be negative")
        return price
    
    
    def calculate_tax(self, product):
        return round(product.price * Decimal(1.1), 2)

    
class SimpleUserSerializers(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(
        method_name="get_current_user_name"
    )
    class Meta:
        model = get_user_model()
        fields = ["id", "name"]
        
    def get_current_user_name(self,obj):
        return obj.get_full_name()

class ReviwSerializers(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(method_name="get_user")
    
    class Meta:
        model = Review
        fields = ["id", "user", "ratings", "product", "comment"]
        read_only_fields = ["user", "product"]
    
    def get_user(self, obj):
        return SimpleUserSerializers(obj.user).data
        
    def create(self, validated_data):
        product_id = self.context["product_id"]
        return Review.objects.create(product_id=product_id, **validated_data)
    
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        pass