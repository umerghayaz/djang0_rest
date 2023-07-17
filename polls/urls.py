from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
path('student/', StudentAPI.as_view()),
path('register/', RegisterAPI.as_view()),

path('student/<int:id>', StudentAPI.as_view()),
# path('api-token-auth/', views.obtain_auth_token)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('', views.index),
    # path('notes/', views.save_data, name="notes"),
    # path('update/<id>', views.update_data),
    # path('delete_data/<id>', views.delete_data),
    # path('api/token/', views.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', views.as_view(), name='token_refresh'),
]