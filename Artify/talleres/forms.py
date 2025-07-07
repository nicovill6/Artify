from django import forms
from .models import Cursos, Instructor, Inscripciones

class CursoForm(forms.ModelForm):
    
    class Meta:
        model = Cursos
        fields = ['nombre', 'descripcion', 'precio', 'imagen_1', 'imagen_2', 'imagen_3', 'slug']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del curso'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del curso', 'rows': 4}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio del curso'}),
            'imagen_1': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'imagen_2': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'imagen_3': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Url del curso'}),
        }

        labels = {
            'nombre':'Nombre:', 'descripcion':'Descripción:', 'precio':'Precio:', 'imagen_1':'Imagen 1:', 'imagen_2':'Imagen 2:', 'imagen_3':'Imagen 3:', 'slug':' URL:',
        }

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['nombre', 'biografia', 'foto', 'cursos']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del instructor'}),
            'biografia': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Biografía del instructor', 'rows': 4}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'cursos': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'nombre':'Nombre:', 'Biografia':'Biografía:', 'foto':'Foto:', 'cursos':'Cursos:',
        }

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripciones
        fields = ['curso', 'alumnos', 'valoracion']
        widgets = {
            'curso': forms.Select(attrs={'class': 'form-control'}),
            'alumnos': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingresar Alumno'} ),
            'valoracion': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'curso': 'Curso:',
            'alumnos': 'Alumno:',
            'valoracion': 'Valoración:',
        }


