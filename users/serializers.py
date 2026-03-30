from djoser.serializers import UserCreateSerializer as BaseUserCreateSerrializers
from djoser.serializers import UserSerializer as BaseUserSerializers


class UserCreateSerializer(BaseUserCreateSerrializers):
    class Meta(BaseUserCreateSerrializers.Meta):
        ref_name = "CustomUserCreateSerializer"
        fields = [
            'id',
            "email",
            'password',
            'first_name',
            "last_name",
            "address",
            "phone_number"
        ]


class UserSerializer(BaseUserSerializers):
    class Meta(BaseUserSerializers.Meta):
        ref_name = "CustomUserSerializer"
        fields = [
            "email",
            'first_name',
            "last_name",
            "address",
            "phone_number",
            "is_staff",
            "is_active",
        ]
        read_only_fields = ["is_staff", "is_active"]