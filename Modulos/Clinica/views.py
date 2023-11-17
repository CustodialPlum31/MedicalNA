from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from .forms import LoginForm
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
        
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'index0.html')

def register(request):
    return render(request,'register.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirige a la página deseada después del inicio de sesión
                return redirect('nombre_de_la_vista_o_ruta')
            else:
                # El inicio de sesión falló
                return render(request, 'login.html', {'form': form, 'error': 'Credenciales inválidas.'})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

