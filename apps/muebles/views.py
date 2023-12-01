from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import MuebleSerializer


class MueblesListView(generics.ListAPIView):
  """
  Permite ver una lista completa de todos los Muebles
  """
  queryset = MuebleSerializer.Meta.model.objects.all()
  serializer_class = MuebleSerializer


class MuebleDetailView(generics.RetrieveAPIView):
  """
  Permite ver el detalle de un Mueble
  """
  queryset = MuebleSerializer.Meta.model.objects.all()
  serializer_class = MuebleSerializer


class MuebleViewSet(viewsets.ModelViewSet):
  """
  Permite hacer un CRUD sobre el modelo Mueble(solo para usuarios administradores)
  """
  permission_classes = [IsAuthenticated, IsAdminUser]
  queryset = MuebleSerializer.Meta.model.objects.all()
  serializer_class = MuebleSerializer