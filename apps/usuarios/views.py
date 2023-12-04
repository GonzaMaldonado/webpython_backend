from rest_framework import viewsets, views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer, UserSerializer


class Login(TokenObtainPairView):
  serializer_class = MyTokenObtainPairSerializer


class Register(views.APIView):

  def post(self, request, *args, **kwargs):
    user_serializer = RegisterSerializer(data=request.data)

    if user_serializer.is_valid():
      user_serializer.save()
      login = MyTokenObtainPairSerializer(data=request.data)
      if login.is_valid():
        return Response({
          'access': login.validated_data.get('access'),
          'refresh': login.validated_data.get('refresh')
        }, status=status.HTTP_201_CREATED)
      
    return Response({'message': 'Existen errores en el registro', 'error': user_serializer.errors
                         },status=status.HTTP_400_BAD_REQUEST)


class Logout(views.APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user', 0))

        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Sesión cerrada exitosamente'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'Credenciales invalidas'}, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer