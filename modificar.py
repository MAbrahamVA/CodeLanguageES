from utilidades import *

def modificar():
    idBuscado = input("Ingrese ID a modificar: ")
    if idBuscado in IDLeng:
        pos = IDLeng.index(idBuscado)
        nombreLeng[pos] = input("Nuevo nombre: ")
        creador[pos] = input("Nuevo creador: ")
        anioCreacion[pos] = input("Nuevo año: ")
        paradigmas[pos] = input("Nuevos paradigmas: ")
        popularidad[pos] = input("Nueva popularidad: ")
        usoPrincipal[pos] = input("Nuevo uso principal: ")
        descripcion[pos] = input("Nueva descripción: ")
        guardar_datos()
        print("Modificación completada.")
    else:
        print("ID no encontrado.")
