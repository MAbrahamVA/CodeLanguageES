//Nombre del Autor: Marlon Emanuel Aguilar Ortega
//fecha: 4/7/2025
//Version: 1.0
//Descripcion:
Algoritmo modificar lenguaje
    Definir opcion, i, n, pos, j Como Entero
    Definir idBuscado, respuesta, confirmacion Como Cadena
    Dimension IDLeng[101], nombreLeng[101], creador[101], añoCreacion[101]
    Dimension paradigmas[101], popularidad[101], usoPrincipal[101], descripcion[101]
	
    Escribir "Ingrese ID a modificar:"
    Leer idBuscado
    pos <- 0
	
    Para i <- 1 Hasta n Hacer
        Si IDLeng[i] = idBuscado Entonces
            pos <- i
        FinSi
    FinPara
	
    Si pos > 0 Entonces
        Escribir "Nuevo nombre:"
        Leer nombreLeng[pos]
        Escribir "Nuevo creador:"
        Leer creador[pos]
        Escribir "Nuevo año:"
        Leer añoCreacion[pos]
        Escribir "Nuevos paradigmas:"
        Leer paradigmas[pos]
        Escribir "Nueva popularidad:"
        Leer popularidad[pos]
        Escribir "Nuevo uso principal:"
        Leer usoPrincipal[pos]
        Escribir "Nueva descripción:"
        Leer descripcion[pos]
        Escribir "Modificación completada."
    Sino
        Escribir "ID no encontrado."
    FinSi
FinAlgoritmo