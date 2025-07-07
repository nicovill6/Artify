from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import  Instructor, Cursos, Alumnos, Inscripciones
from .forms import CursoForm, InstructorForm, InscripcionForm
from django.urls import reverse_lazy
from django.http import FileResponse
import os

def descargarInformeAlumnos(request):
    rutaAlumnos = os.path.join('reportes', 'informe_alumnos.txt')
    if os.path.exists(rutaAlumnos):
        return FileResponse(open(rutaAlumnos, 'rb'), as_attachment = True, filename = 'informe_alumnos.txt')

def descargarInformeCursos(request):
    rutaCursos = os.path.join('reportes', 'informe_alumnos.txt')
    if os.path.exists(rutaCursos):
        return FileResponse(open(rutaCursos, 'rb'), as_attachment = True, filename = 'informe_cursos.txt')
    
def cursos(request):
    cursos = Cursos.objects.all()
    return render(request, "core/cursos.html" , {'cursos': cursos})

def instructores(request):
    instructores = Instructor.objects.all()
    return render(request, 'core/instructores.html', {'instructores': instructores})

class InstructorListView(ListView):
    model = Instructor
    template_name = 'talleres/instructores_list.html'
    context_object_name = 'instructores'

class InstructorDetailView(DetailView):
    model = Instructor
    template_name = 'talleres/instructores_detail.html'
    context_object_name = 'instructor'
    pk_url_kwarg = 'id'

class InstructorCreateView(CreateView):
    model = Instructor
    form_class = InstructorForm
    template_name = 'talleres/instructor_form.html'
    success_url = reverse_lazy('instructor_list')

class InstructorUpdateView(UpdateView):
    model = Instructor
    template_name = 'talleres/instructor_form.html'
    form_class = InstructorForm
    success_url = reverse_lazy('instructor_list')

    def get_success_url(self):
        return reverse_lazy('instructor_detail')

class InstructorDeleteView(DeleteView):
    model = Instructor
    template_name = 'talleres/instructor_delete.html'
    success_url = reverse_lazy('instructor_list')    
    
    def get_success_url(self):
        return reverse_lazy('instructor_list')

class CursoListView(ListView):
    model = Cursos
    template_name = 'talleres/cursos_list.html'
    context_object_name = 'cursos'

class CursoDetailView(DetailView):
    model = Cursos
    template_name = 'talleres/cursos_detail.html'
    context_object_name = 'curso'
    pk_url_kwarg = 'id' 

class CursoCreateView(CreateView):
    model = Cursos
    form_class = CursoForm
    success_url = reverse_lazy('curso_list')

class CursoUpdateView(UpdateView):
    model = Cursos
    template_name = 'talleres/cursos_form.html'
    form_class = CursoForm
    success_url = reverse_lazy('curso_list')

    def get_succes_url(self):
        return reverse_lazy('curso_detail')

class CursoDeleteView(DeleteView):
    model = Cursos
    template_name = 'talleres/curso_delete.html'
    success_url = reverse_lazy('curso_list')

    def get_success_url(self):
        return reverse_lazy('curso_list')

class AlumnoListView(ListView):
    model = Inscripciones
    template_name = 'talleres/alumnos_list.html'
    context_object_name = 'inscripciones'
    
    def get_queryset(self):
        curso_id = self.kwargs.get('curso_id')
        return Inscripciones.objects.filter(curso__id=curso_id).select_related('alumnos')

class AlumnoDetailView(DetailView):
    model = Alumnos
    template_name = 'talleres/alumnos_detail.html'
    context_object_name = 'alumno'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['curso_id'] = self.request.GET.get('curso_id')
        return context

class InscripcionCreateView(CreateView):
    model = Inscripciones
    form_class = InscripcionForm
    success_url = reverse_lazy('curso_list')
    template_name = 'talleres/inscripciones_form.html'

    def get_initial(self):
        curso_id = self.kwargs.get('curso_id')
        return {'curso': curso_id}  