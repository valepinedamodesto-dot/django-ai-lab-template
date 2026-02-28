from django.shortcuts import render, get_object_or_404
from .models import Producto, Pedido, Cliente
# Create your views here.
'''
Vista de inicio
Solo muestra una plantilla básica sin datos
'''

def home(request):
    return render(request, "tienda/home.html", {})


'''

Vista para listar productos

'''

def lista_productos(request):
    productos = Producto.objects.all().order_by("nombre")
    return render (request, "tienda/lista_productos.html", {"productos": productos})




def detalle_producto(request, pk):

    producto = get_object_or_404(Producto)
    return render(request, "tienda/detalle_producto.html", {"producto": producto}),



