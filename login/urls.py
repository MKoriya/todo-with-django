from django.urls import path
from login.views import loginView, signUpView, homeView, logoutView

urlpatterns = [
    path('', homeView, name='home'),
    path('login/', loginView, name='login'),
    path('signup/', signUpView, name='signup'),
    path('logout/', logoutView, name='logout')
]