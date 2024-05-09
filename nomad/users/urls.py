from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import Me, SignUpView

urlpatterns = [
    path("me", Me.as_view()),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]