from utilidades import *

def mostrar():
    if len(IDLeng) == 0:
        print("No hay lenguajes registrados.")
    else:
        for i in range(len(IDLeng)):
            print(f"=== Lenguaje #{i+1} ===")
            print("ID:", IDLeng[i])
            print("Nombre:", nombreLeng[i])
            print("Creador:", creador[i])
            print("Año:", anioCreacion[i])
            print("Paradigmas:", paradigmas[i])
            print("Popularidad:", popularidad[i])
            print("Uso:", usoPrincipal[i])
            print("Descripción:", descripcion[i])
            print("-----------------------------")
