from django.db import models

# Create your models here.

class Cursos(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Curso")
    descripcion = models.TextField(max_length=800, verbose_name="Descripción")
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Precio")
    imagen_1 = models.ImageField(upload_to="cursos", verbose_name="Imagen 1")
    imagen_2 = models.ImageField(upload_to="cursos", verbose_name="Imagen 2")
    imagen_3 = models.ImageField(upload_to="cursos", verbose_name="Imagen 3")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre
    

class Instructor(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField()
    foto = models.ImageField(upload_to='talleres/')
    cursos=models.ForeignKey(Cursos,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "instructor"
        verbose_name_plural = "instructores"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre


class Alumnos(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='talleres/')
    fecha_nacimiento = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "alumno"
        verbose_name_plural = "alumnos"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre

class Inscripciones(models.Model):
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    alumnos = models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    valoracion = models.IntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name="Valoración (1–5)")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "inscripción"
        verbose_name_plural = "inscripciones"
        ordering = ["-fecha_inscripcion"]

    def __str__(self):
        return f"{self.alumnos.nombre} en {self.curso.nombre}"
