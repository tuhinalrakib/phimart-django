from djoser.serializers import UserCreateSerializer as BaseUserCreateSerrializers, UserSerializer as BaseUserSerializers

class UserCreateSerializer(BaseUserCreateSerrializers):
    class Meta(BaseUserCreateSerrializers.Meta):
        fields = ['id', "email", 'password', 'first_name', "last_name","address","phone_number"]
        
class UserSerializer(BaseUserSerializers):
    class Meta(BaseUserSerializers.Meta):
        fields = ["email",'first_name', "last_name","address","phone_number" ]