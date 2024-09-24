# inventario/producto.py
class Producto:
    def __init__(self, id_producto, nombre, precio, categoria):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * porcentaje / 100

    def cambiar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def mostrar_info(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Categoría: {self.categoria}"
