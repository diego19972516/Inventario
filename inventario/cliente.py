# inventario/cliente.py
from .usuario import Usuario  # Importación relativa

class Cliente(Usuario):
    def __init__(self, nombre, email, direccion):
        super().__init__(nombre, email)
        self.direccion = direccion

    def mostrar_info(self):
        return f"Cliente: {self.nombre}, Dirección: {self.direccion}"
