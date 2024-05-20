from django.urls import path
# from django.contrib.auth.views import LoginView, LogoutView
from .views import Me, JWTLogIn

urlpatterns = [
    path("me", Me.as_view()),
    path('login', JWTLogIn.as_view(), name='login'),
    # path('logout', LogoutView.as_view(next_page='login'), name='logout'),
]
