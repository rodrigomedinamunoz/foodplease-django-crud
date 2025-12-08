from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_platos, name='lista_platos'),
    path('lista/', views.lista_platos, name='lista_platos_lista'),
    path('crear/', views.crear_plato, name='crear_plato'),
    path('eliminar/<int:id>/', views.eliminar_plato, name='eliminar_plato'),
]