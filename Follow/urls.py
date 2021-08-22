from django.urls import path
from . import views

app_name = 'follow'

urlpatterns = [
    path('follow/<int:user_id>/<int:profile_id>/', views.follow, name='follow'),
    path('unfollow/<int:user_id>/<int:profile_id>/', views.unfollow, name='unfollow'),
]