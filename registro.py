from utilidades import *

def registrar():
    while True:
        if len(IDLeng) < 100:
            IDLeng.append(input("ID: "))
            nombreLeng.append(input("Nombre: "))
            creador.append(input("Creador: "))
            anioCreacion.append(input("Año de creación: "))
            paradigmas.append(input("Paradigmas: "))
            popularidad.append(input("Popularidad: "))
            usoPrincipal.append(input("Uso principal: "))
            descripcion.append(input("Descripción: "))
            guardar_datos()
            if input("¿Registrar otro lenguaje? (s/n): ").lower() != "s":
                break
        else:
            print("Límite alcanzado.")
            break
