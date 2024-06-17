from django.urls import path
from accounts.views import AccountView
from rest_framework_simplejwt import views

urlpatterns = [
    path("accounts/", AccountView.as_view()),
    path("login/", views.TokenObtainPairView.as_view()),
    path("login/refresh/", views.TokenRefreshView.as_view()),
]
