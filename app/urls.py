from django.urls import path

from . import views

urlpatterns = [
    path('<str:named_url>/', views.menu, name='menu'),  # http://127.0.0.1:8000/menyu/
]