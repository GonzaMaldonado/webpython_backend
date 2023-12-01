from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import Login, Register, Logout, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
  path('login/', Login.as_view()),
  path('register/', Register.as_view()),
  path('logout/', Logout.as_view()),
  path('refresh/', TokenRefreshView.as_view()),
  path('', include(router.urls)),
]
