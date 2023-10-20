from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def formulario(request):
    return render(request,'formulario.html')

def contactar(request):
    if request.method == "POST":
        asunto = request.POST["asunto"]
        mensaje = request.POST["mensaje"] + " / Email:" + request.POST["email"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["manuelandres82@outlook.com"]
        send_mail(asunto,mensaje, email_desde, email_para, fail_silently=False)
        return render(request,"contactoExitoso.html")
    return render(request,"formulario.html")
        

