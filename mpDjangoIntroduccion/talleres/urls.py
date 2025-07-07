from django.urls import path
from . import views
from .views import InstructorListView, InstructorDetailView, InstructorCreateView, InstructorUpdateView, InstructorDeleteView, CursoListView, CursoDetailView, CursoUpdateView, CursoCreateView, CursoDeleteView, AlumnoDetailView, AlumnoListView, InscripcionCreateView
urlpatterns = [
    path('cursos/', views.cursos, name='cursos'),
    path('instructores/', views.instructores, name='instructores'),
    
    # Instructores URLs

    path('instructores/list/', InstructorListView.as_view(), name='instructor_list'),
    path('instructores/<int:id>/', InstructorDetailView.as_view(), name='instructor_detail'),
    path('crear-Instructor/', InstructorCreateView.as_view(), name='instructor_create'),
    path('editar-Instructor/<int:pk>/', InstructorUpdateView.as_view(), name='instructor_update'),
    path('eliminar-Instructor/<int:pk>/', InstructorDeleteView.as_view(), name='instructor_delete'),
    
    # Cursos URLs
    
    path('cursos/list/', CursoListView.as_view(), name='curso_list'),
    path('cursos/<int:id>/', CursoDetailView.as_view(), name='curso_detail'),
    path('crear-Curso/', CursoCreateView.as_view(), name='curso_create'),
    path('editar-Curso/<int:pk>/', CursoUpdateView.as_view(), name='curso_update'),
    path('eliminar-Curso/<int:pk>/', CursoDeleteView.as_view(), name='curso_delete'),

    # Alumno URLs

    path('curso/<int:curso_id>/alumnos/list/', AlumnoListView.as_view(), name='alumno_list'),
    path('alumnos/<int:id>/', AlumnoDetailView.as_view(), name='alumno_detail'),

    # Inscripciones URLs

    path('crear-inscripciones/<int:curso_id>/', InscripcionCreateView.as_view(), name= 'inscripcion_create'),

]