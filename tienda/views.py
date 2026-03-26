from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Pedido, Cliente
from .forms import ProductoForm
# Create your views here.
'''
Vista de inicio
Solo muestra una plantilla básica sin datos
'''

def home(request):
    return render(request, "tienda/home.html", {})


'''
Vista para listar pedidos
'''
def detalle_pedido(request, pk):
    pedido = get_object_or_404(
        Pedido.objects.select_related("cliente").prefetch_related("productos"),
        pk=pk
    )
    return render(request, "tienda/detalle_pedido.html", {"pedido": pedido})

'''
Vista para listar productos
'''
def lista_productos(request):
    productos = Producto.objects.all().order_by("nombre")
    return render(request, "tienda/lista_productos.html", {"productos": productos})


'''
Vista para detalle de pedido
'''
def detalle_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    return render(request, "tienda/detalle_pedido.html", {"pedido": pedido})


'''
Vista para detalle de producto

'''
def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "tienda/detalle_producto.html", {"producto": producto})

'''
Vista de lista de todos los productod
'''
def lista_pedidos(request):
    pedidos = Pedido.objects.select_related("cliente").prefetch_related("productos").order_by("-fecha")
    return render(request, "tienda/lista_pedidos.html",{"pedidos": pedidos})

'''
Vista de detalle del pedido
'''
def detalle_pedido(request,pk):
    pedido = get_object_or_404(
        Pedido.objects.select_related("cliente").prefetch_related("productos"), pk=pk
    )
    return render(request, "tienda/detalle_pedido.html", {"pedido": pedido})
'''
Vista de detalle de un cliente
'''
def detalle_cliente(request, pk):
    cliente = get_object_or_404(cliente, pk=pk)
    pedidos = Cliente.pedidos.select_related("cliente").prefetch_related("productos").order_by("-fecha")
    return render(
        request,
        "tienda/detalle_cliente.html",
        {
            "cliente" : cliente,
            "pedidos" : pedidos,
        }

    )



def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tienda:lista_productos")
    else:
        form = ProductoForm()

    return render(request, "tienda/crear_producto.html", {"form": form})  


