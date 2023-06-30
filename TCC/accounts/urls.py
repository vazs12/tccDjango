from django.urls import path 
from . import views
from django.shortcuts import redirect

app_name = 'accounts'

urlpatterns = [
    # path('login/', views.login_view, name='login'),
    # path('register/', views.register_view, name='register'),
    path('', views.index, name='index'),
    path('cadastro/', views.StudentCreateView.as_view(), name='cadastro'),
    # path('cadastro/', views.cadastro_view, name='cadastro'),
]
