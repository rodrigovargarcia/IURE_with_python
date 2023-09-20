from django.shortcuts import render, redirect
from .forms import TurnoForm
import mercadopago
from .models import Turno
from datetime import date
from django.http import JsonResponse

def reservar_turno(request):
    context = proceso_pago()
    return render(request, "index.html", context)


def comprobar_formulario(request):
    if request.POST:
        formulario = TurnoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return JsonResponse({'success': 'Su turno fue agendado, realice el pago para confirmar'})
        else:
            if '__all__' in formulario.errors:
                fecha_error = formulario.errors.get('__all__', [])
                error = fecha_error
                return JsonResponse({'error': error})
            if 'fecha' in formulario.errors:
                fecha_error = formulario.errors.get('fecha', [])
                error = fecha_error
            return JsonResponse({'error': error})


def guardar_datos(request):
    turno = Turno.objects.latest('id')
    collection_satus = request.GET.get('collection_status')
    if collection_satus == 'approved':
        turno.pagado = "Si"
        turno.save()
        print(turno)
    else:
        turno.pagado = "No"
    return render(request, 'master.html')


def proceso_pago():
    sdk=mercadopago.SDK('APP_USR-6379049892624308-091120-f48c14cefda645127c7de2b10bf3e3eb-1476562297')
    compra = {
        "items": [
            {
                "title": "Turno con Iure",
                "quantity": 1,
                "currency_id": "ARS",
                "unit_price": 2500  # Precio del producto en ARS
            }
        ],
            "back_urls": {
        "success": "http://127.0.0.1:8000/confirmar/",
        "failure": "http://127.0.0.1:8000/failure",
        "pending": "https://127.0.0.1:8000/pendings"
    },
    "auto_return": "approved",
    #"notification_url": "https://75jqdp2p-8000.brs.devtunnels.ms/guardar"
    }
    fecha = date.today()
    fecha_actual = fecha.strftime("%Y-%m-%d")
    horarios = Turno.HORARIOS
    motivos = Turno.MOTIVOS
    profesionales = Turno.PROFESIONALES
    formulario = TurnoForm()
    preference_response = sdk.preference().create(compra)
    preference = preference_response["response"]
    #print(preference)
    context = {
        "fecha_actual": fecha_actual,
        "preference": preference,
        "motivos": motivos,
        "horarios": horarios,
        "profesionales": profesionales,
        "formulario": formulario,
    }
    return context




# TESTUSER1658953798
# kLAyJMzoIf


#comprador
#TESTUSER419598720
#GJ1rjdmlhI