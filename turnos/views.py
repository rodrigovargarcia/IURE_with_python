from django.shortcuts import render, redirect
from .forms import TurnoForm
import mercadopago
from iure import settings


def reservar_turno(request):
    formulario = TurnoForm(request.POST or None)
    return render(request, 'index.html', {'formulario': formulario})

def home(request):
    return render(request,'index.html')

# <------------------    FUNCION DE PROCESAMIENTO DE PAGOS CON MERCADO PAGO    ---------------------->


# def procesador_pago(request):
#     mp = mercadopago.MP(client_id=settings.MERCADOPAGO_CLIENT_ID, client_secret=settings.MERCADOPAGO_CLIENT_SECRET)

#     preference = {
#         "items": [
#             {
#                 "title": "Consulta",
#                 "quantity": 1,
#                 "currency_id": "ARS",
#                 "unit_price": 3000  # Precio del producto
#             }
#         ]
#     }

#     preference = mp.create_preference(preference)
#     preference_id = preference["response"]["id"]
#     # Redirige al usuario al sitio de MercadoPago para realizar el pago
#     return redirect(preference["response"]["init_point"])