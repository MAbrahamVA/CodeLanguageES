from registro import registrar
from modificar import modificar
from eliminar import eliminar
from mostrar import mostrar

def mostrar_menu():
    print("==== MENÚ ====")
    print("1. Registrar lenguaje")
    print("2. Modificar lenguaje")
    print("3. Eliminar lenguaje")
    print("4. Mostrar lenguajes")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        registrar()
    elif opcion == "2":
        modificar()
    elif opcion == "3":
        eliminar()
    elif opcion == "4":
        mostrar()
    elif opcion == "5":
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida.")
