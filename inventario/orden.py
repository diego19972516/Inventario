# inventario/orden.py
class Orden:
    def __init__(self, id_orden, productos):
        self.id_orden = id_orden
        self.productos = productos  # Lista de productos

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        self.productos.remove(producto)

    def calcular_total(self):
        return sum([producto.precio for producto in self.productos])

    def mostrar_orden(self):
        return [producto.mostrar_info() for producto in self.productos]
