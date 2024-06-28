import csv
import funciones
def agregar_producto():
    print("*** Agregar producto al inventario ***")
    nombre_producto = input("Ingrese el nombre del producto: ")
    categoria_producto = input("Ingrese la categoría del producto (Electrónica, Textil, Calzado): ")
    precio_producto = input("Ingrese el precio del producto: ")

    with open('inventario.csv', 'a', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow([nombre_producto, categoria_producto, precio_producto])

    print("Producto agregado al inventario.")

def leer_inventario():
    print("*** Inventario de productos ***")
    try:
        with open('inventario.csv', 'r', newline='') as archivo_csv:
            reader = csv.reader(archivo_csv)
            for producto in reader:
                print(producto)
    except FileNotFoundError:
        print("El inventario está vacío. Aún no se han agregado productos.")

def clasificar_productos():
    print("*** Clasificación de productos y generación de archivo de texto ***")
    categorias = {
        'Electrónica': [],
        'Textil': [],
        'Calzado': []
    }

    try:
        with open('inventario.csv', 'r', newline='') as archivo_csv:
            reader = csv.reader(archivo_csv)
            next(reader)  
            for producto in reader:
                categoria = producto[2] 
                if categoria in categorias:
                    categorias[categoria].append(producto)

        if any(categorias.values()):
            with open('clasificacion_productos.txt', 'w') as archivo_txt:
                for categoria, productos in categorias.items():
                    if productos:
                        archivo_txt.write(f"{categoria}:\n")
                        for producto in productos:
                            archivo_txt.write(f"{', '.join(producto)}\n")
            print("Archivo de clasificación generado correctamente.")
        else:
            print("No hay productos en el inventario para clasificar.")
    except FileNotFoundError:
        print("El inventario está vacío. Aún no se han agregado productos.")

def menu():
    while True:
        print("\n Gestión de Inventario")
        print("Seleccione una opción:")
        print("1. Agregar producto al inventario")
        print("2. Leer el inventario")
        print("3. Clasificar productos y generar archivo de texto")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            leer_inventario()
        elif opcion == "3":
            clasificar_productos()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")






