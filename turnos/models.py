from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

# Create your models here.
 
def validar_dia(value):
    hoy = date.today()
    semana = date.fromisoformat(f'{value}').weekday()

    if value < hoy:
        raise ValidationError('Por favor, seleccione una fecha valida.')
    if (semana == 5) or (semana == 6):
        raise ValidationError('Por favor, seleccione un día hábil de la semana.')


class Turno(models.Model):
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    fecha = models.DateField(validators=[validar_dia])
    HORARIOS = (
        ('1', '17:00'),
        ('2', '18:00'),
        ('3', '19:00'),
        ('4', '20:00')
    )
    horario = models.CharField(max_length=20, choices=HORARIOS)

    MOTIVOS = (
        ('1', 'Asesoramiento integral.'),
        ('2', 'Gestión de documentos argentinos.'),
        ('3', 'Gestión de documentos italianos.'),
        ('4', 'Juicio por falta de turnos.'),
        ('5', 'Asesoramiento por ciudadanías en Italia.'),
        ('6', 'Asesoramiento por ciudadanías via consulado italiano.')
    )
    motivo = models.CharField(max_length=100, choices=MOTIVOS)

    PROFESIONALES = (
        ('1', 'Dr. Nicolas Vaca Cianferoni'),
        ('2', 'Dra. Agustina Afur')
    )
    profesional = models.CharField(max_length=50, choices=PROFESIONALES)
    telefono = models.IntegerField()
    email = models.CharField(max_length=30)

    class Meta:
        unique_together = ('horario', 'fecha')



    
