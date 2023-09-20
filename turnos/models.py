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
        ('17:00', '17:00'),
        ('18:00', '18:00'),
        ('19:00', '19:00'),
        ('20:00', '20:00')
    )
    horario = models.CharField(max_length=20, choices=HORARIOS)

    MOTIVOS = (
        ('Asesoramiento integral.', 'Asesoramiento integral.'),
        ('Gestión de documentos argentinos.', 'Gestión de documentos argentinos.'),
        ('Gestión de documentos italianos.', 'Gestión de documentos italianos.'),
        ('Juicio por falta de turnos.', 'Juicio por falta de turnos.'),
        ('Asesoramiento por ciudadanías en Italia.', 'Asesoramiento por ciudadanías en Italia.'),
        ('Asesoramiento por ciudadanías via consulado italiano.', 'Asesoramiento por ciudadanías via consulado italiano.')
    )
    motivo = models.CharField(max_length=100, choices=MOTIVOS)

    PROFESIONALES = (
        ('Dr. Nicolas Vaca Cianferoni', 'Dr. Nicolas Vaca Cianferoni'),
        ('Dra. Agustina Afur', 'Dra. Agustina Afur')
    )
    profesional = models.CharField(max_length=50, choices=PROFESIONALES)
    telefono = models.BigIntegerField()
    email = models.CharField(max_length=30)
    pagado = models.CharField(max_length= 2,default='No')

    class Meta:
        unique_together = ('horario', 'fecha')

    def __str__(self):
        return (
            "Nombre: "
            + self.nombre
            + " Apellido: "
            + self.apellido
            + " fecha: "
            + str(self.fecha) 
            + "hora:"
            + self.horario
            + "pagado:"
            + self.pagado
        )

    
