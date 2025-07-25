"""
URL configuration for Artify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views as core_views
from talleres import views as talleres_views

urlpatterns = [
    path('', core_views.home, name='home'),
    path('contacto/', core_views.contacto, name='contacto'),
    path('', include('talleres.urls')),
    path('admin/', admin.site.urls),
    path('reportes/alumnos/', talleres_views.descargarInformeAlumnos, name='descargar_alumnos'),
    path('reportes/cursos/', talleres_views.descargarInformeCursos, name='descargar_cursos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
