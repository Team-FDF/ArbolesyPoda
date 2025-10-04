from django.shortcuts import render, redirect
from .models import cotizador
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def correo(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        mensaje = request.POST.get("mensaje")

        cotizador.objects.create(    
            nombre=nombre,
            email=email,
            mensaje=mensaje
        )

        asunto = "Nuevo mensaje desde la web"
        cuerpo = f"Nombre: {nombre}\nCorreo: {email}\n\nMensaje:\n{mensaje}"

        send_mail(
            asunto,
            cuerpo,
            settings.EMAIL_HOST_USER,          
            ['fabianacevedoplaza@gmail.com'],             
            fail_silently=False,
        )

        return redirect('contacto')
    return render(request,"correo.html")

def contacto(request):
    return render(request, 'contacto.html')

def servicios(request):
    return render(request, 'servicios.html')

def productos(request):
    return render(request, 'productos.html')