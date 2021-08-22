from django.urls import path, include
from . import views


app_name = 'profile'

urlpatterns = [
    path('<int:profile_id>/', views.user_profile, name='user_profile'),
    path('edit/<int:profile_id>/', views.edit_profile, name='edit_profile'),
    path('', include('Follow.urls', namespace='follow')),
]
