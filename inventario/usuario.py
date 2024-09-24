# inventario/usuario.py
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def mostrar_info(self):
        return f"Usuario: {self.nombre}, Email: {self.email}"

class Empleado(Usuario):
    def __init__(self, nombre, email, id_empleado):
        super().__init__(nombre, email)  # Llama al constructor de la clase base
        self.id_empleado = id_empleado

    def mostrar_info(self):
        return f"Empleado: {self.nombre}, Email: {self.email}, ID: {self.id_empleado}"
