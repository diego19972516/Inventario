# inventario/reporte.py
class Reporte:
    def __init__(self, inventario):
        self.inventario = inventario

    def generar_reporte(self):
        return [producto.mostrar_info() for producto in self.inventario.productos]
