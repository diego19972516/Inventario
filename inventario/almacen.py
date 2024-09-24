# inventario/almacen.py
from .inventario import Inventario  # Importación relativa

class Almacen:
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion
        self.inventario = Inventario()

    def agregar_inventario(self, producto):
        self.inventario.agregar_producto(producto)

    def mostrar_inventario(self):
        return self.inventario.mostrar_inventario()
