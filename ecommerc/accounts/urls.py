from django.urls import path
from . import views
from .views import login_view, logout_view, profile_view, register_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('register/', views.register_view, name='register'),
]
