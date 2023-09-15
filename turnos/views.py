from django.shortcuts import render, redirect
from .forms import TurnoForm
from iure import settings
import mercadopago
from .models import Turno

def reservar_turno(request):
    formulario = TurnoForm()
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
        "success": "http://127.0.0.1:8000/",
        "failure": "http://127.0.0.1:8000/failure",
        "pending": "https://127.0.0.1:8000/pendings"
    },
    "auto_return": "approved"
    }
    horarios = Turno.HORARIOS
    motivos = Turno.MOTIVOS
    profesionales = Turno.PROFESIONALES
    
    preference_response = sdk.preference().create(compra)
    preference = preference_response["response"]
    print(preference)
    context = {
        "formulario": formulario,
        "preference": preference,
        "motivos": motivos,
        "horarios": horarios,
        "profesionales": profesionales,
    }
    return render(request, "index.html", context)

# TESTUSER1658953798
# kLAyJMzoIf


#comprador
# TESTUSER1699325211
# H57e2wQIvb