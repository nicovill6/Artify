from django.contrib import admin
from .models import Cursos,Instructor,Inscripciones
from .models import Alumnos
# Register your models here.

admin.site.register(Cursos)
admin.site.register(Instructor)
admin.site.register(Alumnos)
admin.site.register(Inscripciones)
