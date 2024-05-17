import requests
from django.shortcuts import render
# Create your views here.
def productos_aliados(request):
    url = 'http://jorgeavm.top/api/patrons/'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Esto lanzará una excepción si el código de estado HTTP es 4xx o 5xx
        try:
            allays = response.json()
        except ValueError:  # Captura errores de decodificación JSON
            allays = []
    except requests.RequestException as e:  # Captura errores de conexión y otros errores de solicitudes
        allays = []
        print(f"Error al realizar la solicitud: {e}")
    return render(request, 'productos_aliados.html', {'allays': allays})
