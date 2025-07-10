//Nombre del Autor: Marlon Emanuel Aguilar Ortega
//fecha: 4/7/2025
//Version: 1.0
//Descripcion:
Algoritmo eliminar lenguaje
    Definir opcion, i, n, pos, j Como Entero
    Definir idBuscado, respuesta, confirmacion Como Cadena
    Dimension IDLeng[101], nombreLeng[101], creador[101], añoCreacion[101]
    Dimension paradigmas[101], popularidad[101], usoPrincipal[101], descripcion[101]
	
    Escribir "Ingrese ID a eliminar:"
    Leer idBuscado
    pos <- 0
	
    Para i <- 1 Hasta n Hacer
        Si IDLeng[i] = idBuscado Entonces
            pos <- i
        FinSi
    FinPara
	
    Si pos > 0 Entonces
        Escribir "¿Está seguro de que desea eliminar ", nombreLeng[pos], "? (s/n):"
        Leer confirmacion
        Si confirmacion = "s" o confirmacion = "S" Entonces
            Para j <- pos Hasta n - 1 Hacer
                IDLeng[j] <- IDLeng[j+1]
                nombreLeng[j] <- nombreLeng[j+1]
                creador[j] <- creador[j+1]
                añoCreacion[j] <- añoCreacion[j+1]
                paradigmas[j] <- paradigmas[j+1]
                popularidad[j] <- popularidad[j+1]
                usoPrincipal[j] <- usoPrincipal[j+1]
                descripcion[j] <- descripcion[j+1]
            FinPara
            n <- n - 1
            Escribir "Lenguaje eliminado."
        Sino
            Escribir "Eliminación cancelada."
        FinSi
    Sino
        Escribir "ID no encontrado."
    FinSi
FinAlgoritmo
