from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from order.models import Cart, CartItem, Order, OrderItem
from order.serializers import CartSerializer, CartItemsSerializer, CartUpdateSerializer, AddCartItemSerializer, OrderSerializers, CreateOrderSerializer, UpdateOrderSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.
class CartViewSet(CreateModelMixin, RetrieveModelMixin , DestroyModelMixin, GenericViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return Cart.objects.prefetch_related("items__product").filter(user = self.request.user)
    
class CartItemViewSet(ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete"]
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddCartItemSerializer
        elif self.request.method == "PATCH":
            return CartUpdateSerializer
        return CartItemsSerializer
    
    def get_serializer_context(self):
        return {"cart_id" : self.kwargs["cart_pk"]}
    
    def get_queryset(self):
        return CartItem.objects.select_related("product").filter(cart_id=self.kwargs["cart_pk"])
    
class OrderViewSet(ModelViewSet):
    http_method_names = ["get", 'post', 'patch', 'delete', 'head', 'option']
    
    def get_permissions(self):
        if self.request.method == "DELETE":
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateOrderSerializer
        if self.request.method == "PATCH":
            return UpdateOrderSerializer
        return OrderSerializers
    
    def get_serializer_context(self):
        return {
            "user_id":self.request.user.id,
            "user": self.request.user
            }
    
    def get_queryset(self):
        if self.request.user.is_staff == True:
            return Order.objects.prefetch_related("items__product").all()
        return Order.objects.prefetch_related("items__product").filter(user = self.request.user)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)