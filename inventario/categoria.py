# inventario/categoria.py
class Categoria:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

    def mostrar_categoria(self):
        return f"Categoría: {self.nombre}"
