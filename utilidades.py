import os

campos = ["IDLeng.txt", "nombre.txt", "creador.txt", "anio.txt", "paradigmas.txt", "popularidad.txt", "uso.txt", "descripcion.txt"]

if all(os.path.exists(c) for c in campos):
    with open(campos[0], "r") as f: IDLeng = f.read().splitlines()
    with open(campos[1], "r") as f: nombreLeng = f.read().splitlines()
    with open(campos[2], "r") as f: creador = f.read().splitlines()
    with open(campos[3], "r") as f: anioCreacion = f.read().splitlines()
    with open(campos[4], "r") as f: paradigmas = f.read().splitlines()
    with open(campos[5], "r") as f: popularidad = f.read().splitlines()
    with open(campos[6], "r") as f: usoPrincipal = f.read().splitlines()
    with open(campos[7], "r") as f: descripcion = f.read().splitlines()
else:
    IDLeng = []
    nombreLeng = []
    creador = []
    anioCreacion = []
    paradigmas = []
    popularidad = []
    usoPrincipal = []
    descripcion = []

def guardar_datos():
    with open(campos[0], "w") as f: f.write("\n".join(IDLeng))
    with open(campos[1], "w") as f: f.write("\n".join(nombreLeng))
    with open(campos[2], "w") as f: f.write("\n".join(creador))
    with open(campos[3], "w") as f: f.write("\n".join(anioCreacion))
    with open(campos[4], "w") as f: f.write("\n".join(paradigmas))
    with open(campos[5], "w") as f: f.write("\n".join(popularidad))
    with open(campos[6], "w") as f: f.write("\n".join(usoPrincipal))
    with open(campos[7], "w") as f: f.write("\n".join(descripcion))
