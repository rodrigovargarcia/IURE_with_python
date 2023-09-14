from django.shortcuts import render, redirect
from .forms import TurnoForm
from iure import settings
import mercadopago

def reservar_turno(request):
    formulario = TurnoForm()

# TESTUSER1658953798
# kLAyJMzoIf

def success(request):
    formulario = TurnoForm
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
    }
    preference_response = sdk.preference().create(compra)
    preference = preference_response["response"]
    preference['back_urls'] = { 'failure': 'http://127.0.0.1:8000/', 'pending': 'http://127.0.0.1:8000/','success': 'http://127.0.0.1:8000/success/'}
    preference['redirect_urls'] = {'failure': 'http://127.0.0.1:8000/', 'pending': 'http://127.0.0.1:8000/','success': 'http://127.0.0.1:8000/success/'}
    preference['auto_return'] = 'approved'
    print(preference)
    return render(request, 'master.html', {'formulario': formulario, 'preference': preference})

#comprador
# TESTUSER1699325211
# H57e2wQIvb