from django.urls import path
from . import views

app_name = 'phone_login'

urlpatterns = [
    path('', views.login_phone, name='login_phone'),
    path('verify/', views.verify_phone, name='verify_phone'),

]