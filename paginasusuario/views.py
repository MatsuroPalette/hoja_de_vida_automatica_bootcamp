# from django.shortcuts import render
# from django.http import HttpResponse

# def pagina_bienvenida(request):
# 	return HttpResponse()

# # Create your views here.
# from django.shortcuts import render
# from .models import DatosPersonales

# # Fíjate en el nombre que sigue después de "def"
# def index(request): 
#     datos = DatosPersonales.objects.first()
#     return render(request, 'paginasusuario/index.html', {'datos': datos})


#nuevo 1


from django.shortcuts import render
from .models import (
    DatosPersonales,
    ExperienciaLaboral,
    CursosRealizados,
    Reconocimientos,
    Certificado
)

def index(request):
    perfil = DatosPersonales.objects.first()

    experiencias = ExperienciaLaboral.objects.filter(
        perfil=perfil,
        activar_front=True
    )

    cursos = CursosRealizados.objects.filter(
        perfil=perfil,
        activar_front=True
    )

    reconocimientos = Reconocimientos.objects.filter(
        perfil=perfil,
        activar_front=True
    )
    
    certificados = Certificado.objects.filter(
    perfil=perfil,
    activar_front=True
    )


    context = {
        'perfil': perfil,
        'experiencias': experiencias,
        'cursos': cursos,
        'reconocimientos': reconocimientos,
        'certificados': certificados
    }

    return render(request, 'paginasusuario/index.html', context)