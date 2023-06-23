from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('palindromo/<str:word>/', views.palindromo, name='palindromo'),
]