from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('platos/', include('platos.urls')),
    path('mockup/', TemplateView.as_view(template_name='mockup/index.html'), name='mockup'),
    path('', include('platos.urls')),  # Si tienes esto para la raíz
]