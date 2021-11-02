#Aldes Quintero

import sqlite3
BASE_DE_DATOS = "inventario.db"

def obtener_conexion():
    return sqlite3.connect(BASE_DE_DATOS)


def crear_tablas():
    tablas = [
        """
        CREATE TABLE IF NOT EXISTS inventario(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto TEXT NOT NULL,
            descripcion TEXT NOT NULL
        );
        """
    ]
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    for tabla in tablas:
        cursor.execute(tabla)


def principal():
    crear_tablas()
    menu = """
1) Agregar nuevo producto
2) Editar producto existente
3) Eliminar producto existente
4) Ver listado de productos
5) Buscar descripcion de producto
6) Salir
Elige: """
    eleccion = ""
    while eleccion != "6":
        eleccion = input(menu)
        if eleccion == "1":
            producto = input("\nIngresa producto: ")
            # Comprobar si no existe
            posible_descripcion = buscar_descripcion_producto(producto)
            if posible_descripcion:
                print(f"El producto'{producto}' ya existe")
            else:
                descripcion= input("Ingresa la descripcion: ")
                agregar_producto(producto, descripcion)
                print("Producto agregado")
        if eleccion == "2":
            producto = input("\nIngresa el producto que quieres editar: ")
            nueva_descripcion = input("Ingresa la descripcion: ")
            editar_producto(producto, nueva_descripcion)
            print("Producto actualizado")
        if eleccion == "3":
            producto = input("\nIngresa el producto a eliminar: ")
            eliminar_producto(producto)
        if eleccion == "4":
            productos = obtener_productos()
            print("\n========Lista de productos========\n")
            for producto in productos:
                # Al leer desde la base de datos se devuelven los datos como arreglo, por
                # lo que hay que imprimir el primer elemento
                print(producto[0])
        if eleccion == "5":
            producto = input(
                "\nIngresa el producto el cual quieres saber el descripcion: ")
            descripcion = buscar_descripcion_producto(producto)
            if descripcion:
                print(f"La descripción de '{producto}' es:\n{descripcion[0]}")
            else:
                print(f"Producto '{producto}' no encontrada")


def agregar_producto(producto, descripcion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sentencia = "INSERT INTO inventario(producto, descripcion) VALUES (?, ?)"
    cursor.execute(sentencia, [producto, descripcion])
    conexion.commit()


def editar_producto(producto, nueva_descripcion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sentencia = "UPDATE inventario SET descripción = ? WHERE producto = ?"
    cursor.execute(sentencia, [nueva_descripcion, producto])
    conexion.commit()


def eliminar_producto(producto):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sentencia = "DELETE FROM inventario WHERE producto = ?"
    cursor.execute(sentencia, [producto])
    conexion.commit()


def obtener_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    consulta = "SELECT producto FROM inventario"
    cursor.execute(consulta)
    return cursor.fetchall()


def buscar_descripcion_producto(producto):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    consulta = "SELECT descripcion FROM inventario WHERE producto = ?"
    cursor.execute(consulta, [producto])
    return cursor.fetchone()


if __name__ == '__main__':
   principal()