
from django.urls import path
from . import views

urlpatterns = [
      path('register', views.register, name="register"),
      path('logout', views.logout, name="logout"),
      path('login', (views.login_puppy), name="login"),
]
