from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('profile/', include('Profile.urls', namespace='profile')),
    path('phone/', include('Phone.urls', namespace='phone_login')),
]