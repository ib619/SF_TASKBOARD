from django.urls import path
from .views import Membership, otp, greet, otpfail
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('otp/', otp, name='otp'),
    path('signup/', Membership, name='Membership'),
    path('login/', auth_views.LoginView.as_view(template_name='my_login.html'), name='login'),
    path('greet/', greet, name='greet'),
    path('otpfail/', otpfail, name='otpfail'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]