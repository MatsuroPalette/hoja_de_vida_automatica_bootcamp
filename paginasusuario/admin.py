from django.contrib import admin
from .models import (
    DatosPersonales,
    ExperienciaLaboral,
    Reconocimientos,
    CursosRealizados,
    ProductosAcademicos,
    VentaGarage,
    Certificado
)
from django.conf import settings
import os


# ==========================
# DATOS PERSONALES
# ==========================
@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    list_display = (
        'nombres',
        'apellidos',
        'numero_cedula',
        'nacionalidad',
        'sexo',
        'perfil_activo'
    )
    search_fields = ('nombres', 'apellidos', 'numero_cedula')
    list_filter = ('sexo', 'perfil_activo')
    ordering = ('apellidos',)


# ==========================
# EXPERIENCIA LABORAL
# ==========================
@admin.register(ExperienciaLaboral)
class ExperienciaLaboralAdmin(admin.ModelAdmin):
    list_display = (
        'perfil',
        'cargo_desempenado',
        'nombre_empresa',
        'fecha_inicio',
        'fecha_fin',
        'activar_front'
    )
    search_fields = ('cargo_desempenado', 'nombre_empresa')
    list_filter = ('activar_front', 'fecha_inicio')


# ==========================
# RECONOCIMIENTOS
# ==========================
@admin.register(Reconocimientos)
class ReconocimientosAdmin(admin.ModelAdmin):
    list_display = (
        'perfil',
        'tipo_reconocimiento',
        'fecha',
        'entidad_patrocinadora',
        'activar_front'
    )
    list_filter = ('tipo_reconocimiento', 'activar_front')
    search_fields = ('descripcion', 'entidad_patrocinadora')


# ==========================
# CURSOS REALIZADOS
# ==========================
@admin.register(CursosRealizados)
class CursosRealizadosAdmin(admin.ModelAdmin):
    list_display = (
        'perfil',
        'nombre_curso',
        'fecha_inicio',
        'fecha_fin',
        'total_horas',
        'activar_front'
    )
    search_fields = ('nombre_curso',)
    list_filter = ('activar_front',)


# ==========================
# PRODUCTOS ACADÉMICOS
# ==========================
@admin.register(ProductosAcademicos)
class ProductosAcademicosAdmin(admin.ModelAdmin):
    list_display = (
        'perfil',
        'nombre_recurso',
        'clasificador',
        'activar_front'
    )
    search_fields = ('nombre_recurso', 'clasificador')
    list_filter = ('activar_front',)


# ==========================
# VENTA GARAGE
# ==========================
@admin.register(VentaGarage)
class VentaGarageAdmin(admin.ModelAdmin):
    list_display = (
        'perfil',
        'nombre_producto',
        'estado_producto',
        'valor',
        'activar_front'
    )
    list_filter = ('estado_producto', 'activar_front')
    search_fields = ('nombre_producto',)

# ==========================
# CERTIFICADOS
# ==========================
#from .models import Certificado

#-------------------------------------------------------------------------
# @admin.register(Certificado)
# class CertificadoAdmin(admin.ModelAdmin):
#     list_display = ("nombre", "perfil", "fecha", "activar_front")
#     list_filter = ("activar_front",)
#----------------------------------------------------------------------------

# @admin.register(Certificado)
# class CertificadoAdmin(admin.ModelAdmin):
#     list_display = ('nombre', 'perfil', 'activar_front')


# @admin.register(Certificado)
# class CertificadoAdmin(admin.ModelAdmin):
#     list_display = ('nombre', 'perfil', 'activar_front')


@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'perfil', 'activar_front')

    def save_model(self, request, obj, form, change):
        archivo = form.cleaned_data.get('archivo')

        if archivo:
            from azure.storage.blob import BlobServiceClient
            import os
            from django.conf import settings

            blob_service_client = BlobServiceClient(
                account_url=f"https://{settings.AZURE_ACCOUNT_NAME}.blob.core.windows.net",
                credential=settings.AZURE_ACCOUNT_KEY
            )

            nombre_blob = os.path.basename(archivo.name)

            blob_client = blob_service_client.get_blob_client(
                container=settings.AZURE_CONTAINER,
                blob=nombre_blob
            )

            archivo.seek(0)
            blob_client.upload_blob(
                archivo,
                overwrite=True,
                content_type="application/pdf"
            )

            # 🔑 GUARDAMOS SOLO LA URL
            obj.archivo_url = blob_client.url

            # 🔥 ESTO ES LO CRÍTICO
            obj.archivo = None

        super().save_model(request, obj, form, change)
