from rest_framework import serializers
from decimal import Decimal
from product.models import Category,Product, Review

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
    
    """Object Validation"""
    # def validate(self, attrs):
    #     if attrs["password1"] != attrs["password2"]:
    #         raise serializers.ValidationError("Passowrd did not match")
        
    """Override Create Method"""
    # def create(self, validated_data):
    #     product = Product(**validated_data)
    #     product.other= 1
    #     product.save()
    #     return product
    
    """Override Update mathod"""
    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get("email", instance.email)
    #     return instance

class ReviwSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "name", "description"]
        
    def create(self, validated_data):
        product_id = self.context["product_id"]
        return Review.objects.create(product_id=product_id, **validated_data)
        