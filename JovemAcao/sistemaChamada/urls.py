from django.contrib import admin
from django.urls import path
from .views import login

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns = [
    path('login', login.html)
 ]