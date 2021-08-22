from django.urls import path, include
from . import views

app_name = 'post'

urlpatterns = [
    path('details/<slug:slug>/', views.post_details, name='details'),
    path('add/<int:profile_id>/', views.add_post, name='add_post'),
    path('edit/<int:profile_id>/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:profile_id>/<int:post_id>/', views.delete_post, name='delete_post'),
    path('', include('Like.urls', namespace='like')),
]
