# inventario/factura.py
from .orden import Orden  # Importación relativa

class Factura:
    def __init__(self, id_factura, orden: Orden):
        self.id_factura = id_factura
        self.orden = orden

    def generar_factura(self):
        total = self.orden.calcular_total()
        return f"Factura ID: {self.id_factura}, Total: {total}"
