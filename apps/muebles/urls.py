from django.urls import path, include
from .views import MueblesListView, MuebleDetailView, MuebleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'muebles', MuebleViewSet, basename='muebles')

urlpatterns = [
  path('all_muebles/', MueblesListView.as_view()),
  path('mueble/<int:pk>/', MuebleDetailView.as_view()),
  path('', include(router.urls)),
]
