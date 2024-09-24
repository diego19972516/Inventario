# main.py
from inventario.producto import Producto
from inventario.inventario import Inventario
from inventario.cliente import Cliente
from inventario.orden import Orden
from inventario.factura import Factura

def main():
    # Crear productos
    p1 = Producto(1, "Laptop", 1000, "Electrónica")
    p2 = Producto(2, "Smartphone", 500, "Electrónica")

    # Crear inventario y agregar productos
    inventario = Inventario()
    inventario.agregar_producto(p1)
    inventario.agregar_producto(p2)

    # Mostrar inventario
    print("Inventario:")
    for producto in inventario.mostrar_inventario():
        print(producto)

    # Crear orden y factura
    orden = Orden(1, [p1, p2])
    factura = Factura(1, orden)

    # Generar y mostrar factura
    print(factura.generar_factura())

if __name__ == "__main__":
    main()
