from django.core.management.base import BaseCommand
from talleres.models import Alumnos, Cursos, Inscripciones
from django.utils import timezone
import os

def calcularPromedioEdad():
    listaEdades = []
    acumuladorEdades = 0
    contador = 0
    for alumno in Alumnos.objects.all():
        edadAlumno = timezone.now().year - alumno.fecha_nacimiento.year
        listaEdades.append(edadAlumno)
    
    for edades in listaEdades:
        acumuladorEdades+=edades
        contador+=1

    if contador == 0:
        return 0
    return acumuladorEdades/contador

def calcularPromedioCalificacion(inscripciones):
    acumuladorCalificacion = 0
    contador = 0
    for calificacion in inscripciones:
        acumuladorCalificacion+= calificacion.valoracion
        contador+=1
    
    if contador == 0:
        return 0
    
    return acumuladorCalificacion/contador

class Command(BaseCommand):
    mensaje = 'Genera informe de Alumnos y Cursos'

    def handle(self, *args, **kwargs):
        os.makedirs('reportes', exist_ok = True)

        with open('reportes/informe_alumnos.txt', 'w', encoding='UTF-8') as reporteAlumno:
            for alumno in Alumnos.objects.all():
                inscripciones = Inscripciones.objects.filter(alumnos = alumno)
                total = inscripciones.count()
                edad = timezone.now().year - alumno.fecha_nacimiento.year
                reporteAlumno.write(f"Nombre: {alumno.nombre} - Inscripciones: {total} - Edad: {edad} \n")
        
        with open('reportes/informe_alumnos.txt', 'a', encoding='UTF-8') as actualizar:
            actualizar.write(f'\n El promedio de edad de los alumnos es de: {calcularPromedioEdad():.2f}')

        with open('reportes/informe_cursos.txt', 'w', encoding='UTF-8') as reporteCurso:
            for curso in Cursos.objects.all():
                inscripciones = Inscripciones.objects.filter(curso = curso)
                total = inscripciones.count()
                promedioCalificacion = calcularPromedioCalificacion(inscripciones)
                reporteCurso.write(f"Curso: {curso.nombre} - Alumnos total: {total} - Calificacion promedio: {promedioCalificacion:.2f} \n ")