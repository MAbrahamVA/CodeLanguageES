//Nombre del Autor: Marlon Emanuel Aguilar Ortega
//fecha: 4/7/2025
//Version: 1.0
//Descripcion:opcion 1: registrar lenguaje, le permite al usuario registrar un lenguaje
Algoritmo registrar lenguaje
    Definir opcion, i, n, pos, j Como Entero
    Definir idBuscado, respuesta, confirmacion Como Cadena
    Dimension IDLeng[101], nombreLeng[101], creador[101], añoCreacion[101]
    Dimension paradigmas[101], popularidad[101], usoPrincipal[101], descripcion[101]
	
    respuesta <- "s"
    Mientras respuesta = "s" o respuesta = "S" Hacer
        Si n < 100 Entonces
            n <- n + 1
            Escribir "ID:"
            Leer IDLeng[n]
            Escribir "Nombre:"
            Leer nombreLeng[n]
            Escribir "Creador:"
            Leer creador[n]
            Escribir "Año de creación:"
            Leer añoCreacion[n]
            Escribir "Paradigmas:"
            Leer paradigmas[n]
            Escribir "Popularidad:"
            Leer popularidad[n]
            Escribir "Uso principal:"
            Leer usoPrincipal[n]
            Escribir "Descripción:"
            Leer descripcion[n]
            Escribir "¿Registrar otro lenguaje? (s/n):"
            Leer respuesta
        Sino
            Escribir "Límite alcanzado."
            respuesta <- "n"
        FinSi
    FinMientras
FinAlgoritmo