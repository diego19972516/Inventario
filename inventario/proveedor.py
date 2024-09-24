# inventario/proveedor.py
class Proveedor:
    def __init__(self, nombre, empresa, email):
        self.nombre = nombre
        self.empresa = empresa
        self.email = email

    def mostrar_info(self):
        return f"Proveedor: {self.nombre}, Empresa: {self.empresa}, Email: {self.email}"
