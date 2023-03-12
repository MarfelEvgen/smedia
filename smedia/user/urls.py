from django.urls import path
from user.views import *

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('signup/', SignUp.as_view(), name='sign_up'),
    path('login/', UserLogin.as_view(), name='login'),
]