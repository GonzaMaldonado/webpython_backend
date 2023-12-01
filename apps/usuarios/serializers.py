from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)

    token['username'] = user.username
    token['is_staff'] = user.is_staff
    if user.photo != '':
      token['photo'] = user.photo.url
    else:
      token['photo'] = ''

    return token


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
    read_only_field = ('id',)


class RegisterSerializer(serializers.ModelSerializer):
  confirm_password = serializers.CharField(max_length=50, write_only=True)

  class Meta:
    model = User
    fields = '__all__'
    extra_kwargs = {'password': {'write_only': True}}

  def validate(self, attrs):
    password = attrs.get('password')
    confirm_password = attrs.get('confirm_password')

    if password != confirm_password:
      return serializers.ValidationError('Las contraseñas deben ser iguales')
    
    attrs.pop('confirm_password', None)
    return attrs
  
  def create(self, validated_data):
    user = User(**validated_data)
    user.set_password(validated_data['password'])
    user.save()
    return user