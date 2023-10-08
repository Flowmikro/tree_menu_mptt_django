from django.urls import path

from . import views

urlpatterns = [
    path('<str:named_url>/', views.menu, name='menu')
]