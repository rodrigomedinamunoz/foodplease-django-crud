from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # Tus URLs existentes
    path('', views.lista_platos, name='lista_platos'),
    path('lista/', views.lista_platos, name='lista_platos_lista'),
    path('crear/', views.crear_plato, name='crear_plato'),
    path('eliminar/<int:id>/', views.eliminar_plato, name='eliminar_plato'),
    
    # Nueva ruta para el mockup
    path('mockup/', TemplateView.as_view(template_name='mockup/index.html'), name='mockup'),
]