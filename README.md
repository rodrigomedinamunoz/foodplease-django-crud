FoodPlease - CRUD de Platos en Django

Este proyecto corresponde al desarrollo de un CRUD básico en Django, utilizado como parte de la propuesta tecnológica del sistema FoodPlease, una plataforma para gestión y publicación de platos por parte de locales gastronómicos.

El objetivo principal es demostrar un funcionamiento mínimo viable (CRUD) en entorno local, siguiendo buenas prácticas de desarrollo web y sirviendo como base para futuras ampliaciones del proyecto.

Tecnologías utilizadas

Python 3.13
Django 5.2
SQLite (base de datos por defecto)
HTML + Bootstrap 5 para diseño
GitHub para versionamiento y despliegue del repositorio

Funcionalidad del CRUD

Listar platos

Muestra todos los platos registrados.

Crear un nuevo plato

Formulario con:

Nombre

Precio

Descripción

Eliminar plato

Permite borrar un plato por ID.

Este CRUD representa el módulo de gestión de platos para FoodPlease, simulando cómo los locales gestionan su menú.

Ejecutar el proyecto en entorno local

Instalar dependencias

En el directorio del proyecto:

pip install django

Aplicar migraciones

python manage.py makemigrations 
python manage.py migrate

Ejecutar el servidor

python manage.py runserver

Acceder al CRUD

Listado: http://127.0.0.1:8000/platos/

Crear: http://127.0.0.1:8000/platos/crear/

Admin (opcional): http://127.0.0.1:8000/admin/

Modelo Plato
class Plato(models.Model):
nombre = models.CharField(max_length=100) 
precio = models.IntegerField() 
descripcion = models.TextField(blank=True, null=True)

Diseño con Bootstrap

Para una mejor experiencia visual se integró Bootstrap 5 directamente vía CDN en todas las vistas del proyecto.

Próximas mejoras

Este CRUD constituye la base del módulo "Menú del Local" dentro de FoodPlease. En futuras etapas se integrarán:

Edición de platos

Subida de imágenes

Login y roles de usuario

Integración con API REST

Autor

Proyecto desarrollado por Rodrigo Medina, como parte del curso de Desarrollo de Aplicaciones Web.
