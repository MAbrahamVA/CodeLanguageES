
//Nombre del Autor: Marlon Emanuel Aguilar Ortega
//fecha: 4/7/2025
//Version: 1.0
//Descripcion: Elaboracion del Area genereal de registrar lenguajes en donde incluye como agregar, modificar y eliminar un lenguaje.








Algoritmo RegistroLeng
    Definir opcion, i, n, pos, j Como Entero
    Definir idBuscado, respuesta, confirmacion Como Cadena
    Dimension IDLeng[101], nombreLeng[101], creador[101], a�oCreacion[101]
    Dimension paradigmas[101], popularidad[101], usoPrincipal[101], descripcion[101]
	
    n <- 0 
	
    Repetir
        Escribir "==== MEN� ===="
        Escribir "1. Registrar lenguaje"
        Escribir "2. Modificar lenguaje"
        Escribir "3. Eliminar lenguaje"
        Escribir "4. Mostrar lenguajes"
        Escribir "5. Salir"
        Escribir "Seleccione una opci�n:"
        Leer opcion
		
        Segun opcion Hacer
			
            1: 
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
                        Escribir "A�o de creaci�n:"
                        Leer a�oCreacion[n]
                        Escribir "Paradigmas:"
                        Leer paradigmas[n]
                        Escribir "Popularidad:"
                        Leer popularidad[n]
                        Escribir "Uso principal:"
                        Leer usoPrincipal[n]
                        Escribir "Descripci�n:"
                        Leer descripcion[n]
                        Escribir "�Registrar otro lenguaje? (s/n):"
                        Leer respuesta
                    Sino
                        Escribir "L�mite alcanzado."
                        respuesta <- "n"
                    FinSi
                FinMientras
				
            2: 
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
                    Escribir "Nuevo a�o:"
                    Leer a�oCreacion[pos]
                    Escribir "Nuevos paradigmas:"
                    Leer paradigmas[pos]
                    Escribir "Nueva popularidad:"
                    Leer popularidad[pos]
                    Escribir "Nuevo uso principal:"
                    Leer usoPrincipal[pos]
                    Escribir "Nueva descripci�n:"
                    Leer descripcion[pos]
                    Escribir "Modificaci�n completada."
                Sino
                    Escribir "ID no encontrado."
                FinSi
				
            3: 
                Escribir "Ingrese ID a eliminar:"
                Leer idBuscado
                pos <- 0
				
                Para i <- 1 Hasta n Hacer
                    Si IDLeng[i] = idBuscado Entonces
                        pos <- i
                    FinSi
                FinPara
				
                Si pos > 0 Entonces
                    Escribir "�Est� seguro de que desea eliminar ", nombreLeng[pos], "? (s/n):"
                    Leer confirmacion
                    Si confirmacion = "s" o confirmacion = "S" Entonces
                        Para j <- pos Hasta n - 1 Hacer
                            IDLeng[j] <- IDLeng[j+1]
                            nombreLeng[j] <- nombreLeng[j+1]
                            creador[j] <- creador[j+1]
                            a�oCreacion[j] <- a�oCreacion[j+1]
                            paradigmas[j] <- paradigmas[j+1]
                            popularidad[j] <- popularidad[j+1]
                            usoPrincipal[j] <- usoPrincipal[j+1]
                            descripcion[j] <- descripcion[j+1]
                        FinPara
                        n <- n - 1
                        Escribir "Lenguaje eliminado."
                    Sino
                        Escribir "Eliminaci�n cancelada."
                    FinSi
                Sino
                    Escribir "ID no encontrado."
                FinSi
				
            4: 
                Si n = 0 Entonces
                    Escribir "No hay lenguajes registrados."
                Sino
                    Para i <- 1 Hasta n Hacer
                        Escribir "=== Lenguaje #", i, " ==="
                        Escribir "ID: ", IDLeng[i]
                        Escribir "Nombre: ", nombreLeng[i]
                        Escribir "Creador: ", creador[i]
                        Escribir "A�o: ", a�oCreacion[i]
                        Escribir "Paradigmas: ", paradigmas[i]
                        Escribir "Popularidad: ", popularidad[i]
                        Escribir "Uso: ", usoPrincipal[i]
                        Escribir "Descripci�n: ", descripcion[i]
                        Escribir "-----------------------------"
                    FinPara
                FinSi
				
            5:
                Escribir "Programa finalizado."
				
            De Otro Modo:
                Escribir "Opci�n inv�lida."
				
        FinSegun
        Escribir ""
    Hasta Que opcion = 5

FinAlgoritmo

