from django.shortcuts import render, redirect
from .forms import TurnoForm
import mercadopago
from .models import Turno
from datetime import date
from django.http import JsonResponse
from local_settings import ACCESS_TOKEN
from local_settings import NOTIFICACION_URL


def reservar_turno(request):
    context = proceso_pago()
    return render(request, "index.html", context)


def comprobar_formulario(request):
    if request.POST:
        formulario = TurnoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return JsonResponse({'success': 'Su turno fue agendado'})
        else:
            if '__all__' in formulario.errors:
                fecha_error = formulario.errors.get('__all__', [])
                error = fecha_error
                return JsonResponse({'error': error})
            if 'fecha' in formulario.errors:
                fecha_error = formulario.errors.get('fecha', [])
                error = fecha_error
            return JsonResponse({'error': error}, status=405)


def guardar_datos(request):
    turno = Turno.objects.latest('id')
    collection_satus = request.GET.get('collection_status')
    if collection_satus == 'approved':
        turno.pagado = "Si"
        turno.save()
    else:
        turno.pagado = "No"
    return render(request, 'master.html')


def proceso_pago():
    sdk = mercadopago.SDK(
        ACCESS_TOKEN)
    compra = {
        "items": [
            {
                "title": "Turno con Iure",
                "quantity": 1,
                "currency_id": "ARS",
                "unit_price": 7000  # Precio del producto en ARS
            }
        ],
        "back_urls": {
            "success": NOTIFICACION_URL + "/confirmar/",
            "failure": "http://127.0.0.1:8000/failure",
            "pending": "https://127.0.0.1:8000/pendings"
        },
        "auto_return": "approved",
        "notification_url": NOTIFICACION_URL + "/guardar"
    }
    fecha = date.today()
    fecha_actual = fecha.strftime("%Y-%m-%d")
    horarios = Turno.HORARIOS
    motivos = Turno.MOTIVOS
    profesionales = Turno.PROFESIONALES
    formulario = TurnoForm()
    preference_response = sdk.preference().create(compra)
    preference = preference_response["response"]
    context = {
        "fecha_actual": fecha_actual,
        "preference": preference,
        "motivos": motivos,
        "horarios": horarios,
        "profesionales": profesionales,
        "formulario": formulario,
    }
    return context


