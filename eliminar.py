from utilidades import *

def eliminar():
    idBuscado = input("Ingrese ID a eliminar: ")
    if idBuscado in IDLeng:
        pos = IDLeng.index(idBuscado)
        confirmacion = input(f"¿Está seguro de que desea eliminar {nombreLeng[pos]}? (s/n): ")
        if confirmacion.lower() == "s":
            IDLeng.pop(pos)
            nombreLeng.pop(pos)
            creador.pop(pos)
            anioCreacion.pop(pos)
            paradigmas.pop(pos)
            popularidad.pop(pos)
            usoPrincipal.pop(pos)
            descripcion.pop(pos)
            guardar_datos()
            print("Lenguaje eliminado.")
        else:
            print("Eliminación cancelada.")
    else:
        print("ID no encontrado.")
