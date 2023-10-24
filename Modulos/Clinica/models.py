from django.db import models
from datetime import date
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

# Create your models here.

#Elementos que se reflejan en las bd, como tablas ORM

class Medico(models.Model):
    idMed = models.AutoField(primary_key=True)
    nomMed =  models.CharField(max_length=20)
    apeMed = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=20)
    cedula = models.CharField(max_length=18)
    correoMed = models.EmailField()
    contraMed = models.CharField(max_length=128) #Es inseguro guardar contrasenas en la BD
    
    def __str__(self):
        txt = "{0}/{1} {2}({3})"
        return txt.format(self.especialidad,self.nomMed,self.apeMed,self.cedula)
    
"""   
from django.contrib.auth.models import User

# Crear un usuario
usuario = User.objects.create(username='ejemplo', password=make_password('contraseña'))

# Verificar contraseña
if check_password('contraseña', usuario.password):
    # La contraseña es correcta
else:
    # La contraseña es incorrecta
"""
    

    
class Paciente(models.Model):
  
        idPac = models.AutoField(primary_key=True)
        #medicop = models.ForeignKey(Medico, null=False,blank=False,on_delete=models.PROTECT,related_name='pacientes_medico')
        medico = models.ForeignKey(Medico, null = False, blank = False, on_delete=models.PROTECT,default=1)
        nomPac =  models.CharField(max_length=20)
        apePac = models.CharField(max_length=20)
        direccion =  models.CharField(max_length=30)
        correoPac = models.EmailField()
        contraPac = models.CharField(max_length=128)
        telPac = models.CharField(
        max_length=10,  # Ahora la longitud máxima es 10
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message="El número de teléfono debe tener 10 dígitos."
            ),
        ]
    )
        fechanaci = models.DateField(default=date.today)
        
        sexos = [('F','Femenino'),('M','Masculino'),('O','Otros')]
        sexo = models.CharField(max_length=1, choices=sexos)
    
        
        def nombreCompleto(self):
            txt = "{0},{1} "
            return txt.format(self.apePac, self.nomPac)
        
        def __str__(self):
            txt = "{0}/{1}{2}/{3}"
            return txt.format(self.idPac,self.apePac, self.nomPac,self.fechanaci)
        

        
class Consulta(models.Model):
    idConsulta =  models.AutoField(primary_key=True)
    medico = models.ForeignKey(Medico, null = False,blank = False, on_delete=models.CASCADE, default = 1)
    paciente = models.ForeignKey(Paciente, null=False,blank=False,on_delete=models.CASCADE,default=1)
    fecha =  models.DateField(default=date.today)
    hora =  models.TimeField
    diag =  models.CharField(max_length=1028)
    
    def __str__(self):
            txt = "{0}"
            return txt.format(self.idConsulta)
    
class Expediente(models.Model):
    idEx = models.AutoField(primary_key=True)
    medico = models.ForeignKey(Medico, null=False,blank=False,on_delete=models.PROTECT,default=1)
    paciente = models.ForeignKey(Paciente, null=False,blank=False,on_delete=models.PROTECT,default=1)
    diag = models.TextField
    def __str__(self):
        txt = "{0}"
        return txt.format(self.idEx)
    
    
class Administrador(models.Model):
    idAd =  models.AutoField(primary_key=True)
    nomAdm =  models.CharField(max_length=20)
    apeAdm = models.CharField(max_length=20)           
    correoAd = models.EmailField()
    contraAd = models.CharField(max_length=128)
    telAd =models.CharField(
        max_length=10,  # Ahora la longitud máxima es 10
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message="El número de teléfono debe tener 10 dígitos."
            ),
        ]
    )
    def __str__(self):
        txt = "{0}/{1}"
        return txt.format(self.idAd,self.correoAd)
    
    
class Estudio(models.Model):
    idEst =  models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, null=False,blank=False,on_delete=models.PROTECT,default=1)
    nomEst = models.CharField(max_length=15)
    resu = models.CharField(max_length=1024)
    #idPaciente    
    def __str__(self):
        txt = "{0}/{1}"
        return txt.format(self.idEst,self.nomEst)
    
    
        
        
        