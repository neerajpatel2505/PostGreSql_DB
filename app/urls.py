from django.urls import path
from .views import home, regeister , data, login

urlpatterns = [
    path("",home,name='home'),
    path("register/",regeister,name="regeister"),
    path('data/',data,name='data'),
    path('login/',login,name='login')
]