import collections
import pymongo

from pymongo import MongoClient

cluster = MongoClient(
    "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000L")
db = cluster["MongoDB"]
collection = db["Diccionario Slang"]


def VerificarPalabraExistente(Palabra):
    verificar = collection.find_one(
        {"palabra": Palabra})
    if(verificar == None):
        return False
    else:
        return True


def ActualizarPalabra(AntiguaPalabra, NuevaPalabra, NuevaDefinicion):
    collection.update_one({"palabra": AntiguaPalabra}, {"$set": {
        "palabra": NuevaPalabra,
        "definicion": NuevaDefinicion
    }})


def BorrarPalabra(Palabra):
    collection.delete_one({"palabra": Palabra})


def MostrarPalabras():
    palabras = collection.find()
    i = 0
    for row in palabras:
        i += 1
        print(
            f'{i}. Palabra: {row["palabra"]} Definicion: {row["definicion"]}')


while True:

    # Menú de opciones
    print("\n ***** Ingrese la opción deseada ****\n")

    Opcion = int(input(" 1). Agregar nueva palabra \n 2). Editar palabra existente \n 3). Eliminar palabra existente \n 4). Ver listado de palabras \n 5). Buscar significado de palabra \n 6). Salir \n"))

    if(Opcion == 1):
       # Se introduce palabra y definición
        EntradaPalabra = input("\nIngrese palabra a agregar:\n")
        EntradaDefinicion = input("\nIngrese definición:\n")
        if(len(EntradaPalabra) and len(EntradaDefinicion)):

            if(VerificarPalabraExistente(EntradaPalabra)):
                print("\nEsta palabra ya existe ¡por favor! agregue otra palabra")
            else:
                collection.insert_one({
                    "palabra": EntradaPalabra,
                    "definicion": EntradaDefinicion
                })
        else:
            print("\n Por favor llenar ambos campos de informacion")

    elif(Opcion == 2):
        EntradaPalabra = input("\nIngrese la palabra que desea modificar: \n")

        NewWord = input("\nIngrese el nuevo valor de esta palabra: \n")

        NewDefinition = input("\nIngrese la nueva definicion de la palabra: \n")

        if(len(NewWord) and len(NewDefinition) and len(EntradaPalabra)):
            if(VerificarPalabraExistente(EntradaPalabra)):
                ActualizarPalabra(EntradaPalabra, NewWord, NewDefinition)
            else:
                print("\n La palabra no existe!, vuelva a intentarlo")

        else:
            print("\n Por favor llenar los campos de informacion")

    elif(Opcion == 3):
        EntradaPalabra = input("\n Ingrese la palabra que desea eliminar \n")

        if(len(EntradaPalabra)):
            if(VerificarPalabraExistente(EntradaPalabra)):
                BorrarPalabra(EntradaPalabra)

            else:
                print("\n La palabra no existe!")

        else:
            print("\n Por favor llenar los campos de informacion")

    elif(Opcion == 4):
        MostrarPalabras()
    elif(Opcion == 5):
        EntradaPalabra = input("\n Ingrese la palabra que desea ver su significado \n")
        if(len(EntradaPalabra)):
            if(VerificarPalabraExistente(EntradaPalabra)):
                getPalabra = collection.find_one({"palabra": EntradaPalabra})
                print(f'La definicion es: {getPalabra["definicion"]}')
            else:
                print("\n La palabra no existe!")

        else:
            print("\n Por favor llenar los campos de informacion")

    elif(Opcion == 6):
        break

    else:
        print("\n Ingrese una opcion valida \n")
