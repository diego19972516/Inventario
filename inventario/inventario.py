# inventario/inventario.py
from .producto import Producto  # Cambiado para usar importación relativa

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.id_producto != id_producto]

    def buscar_producto(self, id_producto):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                return producto
        return None

    def mostrar_inventario(self):
        return [producto.mostrar_info() for producto in self.productos]
