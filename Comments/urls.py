from django.urls import path
from Comments import views

app_name = 'comment'

urlpatterns = [
    path('add_reply/<int:post_id>/<int:cm_id>/', views.add_reply, name='add_reply'),
]