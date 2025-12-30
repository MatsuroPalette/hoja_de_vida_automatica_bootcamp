from django.db import models

# Create your models here.
class DatosPersonales(models.Model):
    descripcion_perfil = models.CharField(max_length=50)
    perfil_activo = models.IntegerField()
    apellidos = models.CharField(max_length=60)
    nombres = models.CharField(max_length=60)
    nacionalidad = models.CharField(max_length=20)
    lugar_nacimiento = models.CharField(max_length=60)
    fecha_nacimiento = models.DateField()
    numero_cedula = models.CharField(max_length=10, unique=True)
    
    SEXO_CHOICES = [('H', 'Hombre'), ('M', 'Mujer')]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    
    estado_civil = models.CharField(max_length=50)
    licencia_conducir = models.CharField(max_length=6, blank=True, null=True)
    telefono_convencional = models.CharField(max_length=15, blank=True, null=True)
    telefono_fijo = models.CharField(max_length=15, blank=True, null=True)
    direccion_trabajo = models.CharField(max_length=50, blank=True, null=True)
    direccion_domiciliaria = models.CharField(max_length=50)
    sitio_web = models.URLField(max_length=60, blank=True, null=True)

    # def _str_(self): #antes iba así
    #     return f"{self.nombres} {self.apellidos}"
    
    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

# 2. EXPERIENCIA LABORAL
class ExperienciaLaboral(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    cargo_desempenado = models.CharField(max_length=100)
    nombre_empresa = models.CharField(max_length=50)
    lugar_empresa = models.CharField(max_length=50)
    email_empresa = models.EmailField(max_length=100)
    sitio_web_empresa = models.URLField(max_length=100, blank=True)
    nombre_contacto = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=60)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    descripcion_funciones = models.TextField(max_length=100)
    activar_front = models.BooleanField(default=True)
    ruta_certificado = models.CharField(max_length=100, blank=True)

# 3. RECONOCIMIENTOS
class Reconocimientos(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    TIPO_CHOICES = [('Académico', 'Académico'), ('Público', 'Público'), ('Privado', 'Privado')]
    tipo_reconocimiento = models.CharField(max_length=100, choices=TIPO_CHOICES)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=100)
    entidad_patrocinadora = models.CharField(max_length=100)
    activar_front = models.BooleanField(default=True)

# 4. CURSOS REALIZADOS
class CursosRealizados(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombre_curso = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    total_horas = models.IntegerField()
    entidad_patrocinadora = models.CharField(max_length=100)
    activar_front = models.BooleanField(default=True)

# 5. PRODUCTOS ACADÉMICOS Y LABORALES (Se pueden unificar o separar)
class ProductosAcademicos(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombre_recurso = models.CharField(max_length=100)
    clasificador = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    activar_front = models.BooleanField(default=True)

# 6. VENTA GARAGE
class VentaGarage(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=100)
    ESTADO_CHOICES = [('Bueno', 'Bueno'), ('Regular', 'Regular')]
    estado_producto = models.CharField(max_length=40, choices=ESTADO_CHOICES)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    activar_front = models.BooleanField(default=True)
    
#7. Certificados (vamos a ver si funciona)
class Certificado(models.Model):
    perfil = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        related_name="certificados"
    )
    nombre = models.CharField(max_length=100)
    ruta_archivo = models.CharField(max_length=255)
    fecha = models.DateField(null=True, blank=True)
    activar_front = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

