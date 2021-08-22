from django.urls import path
from . import views

app_name = 'like'

urlpatterns = [
    path('post_like/<int:post_id>/', views.post_like, name='post_like'),
    path('post_unlike/<int:post_id>/', views.post_unlike, name='post_unlike'),
]