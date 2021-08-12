from typing import Pattern
from knox import views as knox_views
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, LoginAPI, jobViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('jobs', jobViewSet)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/', RegisterView.as_view()),
    # path('login/', LoginView.as_view()),
    path('postedjobs/', include(router.urls), name='jobs'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-token-auth/', obtain_auth_token),
    # knox
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]