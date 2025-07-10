"""
Creador:Angel A. Lopez C.
Fecha:4/07/2025
Version: 1.0
Descripcion:Modificar el rol de usuarios para darle acceso al menu de desarrollador, roles como: colaboradorr o usuario PLUS,entre otros.
"""

import os

ARCHIVO = "usuarios.txt"

def cargar_usuarios():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            return [line.strip() for line in f if line.strip()]
    else:
        # Si no existe, lo inicializamos con algunos usuarios
        usuarios_iniciales = ["Ana", "Luis", "María", "Carlos"]
        guardar_usuarios(usuarios_iniciales)
        return usuarios_iniciales

def guardar_usuarios(lista):
    with open(ARCHIVO, "w") as f:
        for usuario in lista:
            f.write(usuario + "\n")

def mostrar_menu():
    usuarios = cargar_usuarios()
    cambiar = False
    guardar = False

    while True:
        print("---------- MENÚ DE USUARIOS ----------")
        print("1. Ver usuarios")
        print("2. Modificar un usuario")
        print("3. Guardar cambios")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Lista actual de usuarios:")
            for i, usuario in enumerate(usuarios, start=1):
                print(f"{i}. {usuario}")

        elif opcion == "2":
            try:
                num = int(input(f"Ingrese el número del usuario a modificar (1 a {len(usuarios)}): "))
                if 1 <= num <= len(usuarios):
                    original = usuarios[num - 1]
                    print(f"Usuario seleccionado: {original}")
                    print("Seleccione el nuevo rol:")
                    print("1. Cambiar a Desarrollador")
                    print("2. Cambiar a Colaborador")
                    print("3. Cambiar a Usuario Plus")
                    sub = input("Ingrese una opción: ")

                    if sub == "1":
                        nuevo_nombre = original + " (Desarrollador)"
                    elif sub == "2":
                        nuevo_nombre = original + " (Colaborador)"
                    elif sub == "3":
                        nuevo_nombre = original + " (Usuario Plus)"
                    else:
                        print("Rol inválido. No se realizaron cambios.")
                        nuevo_nombre = ""

                    if nuevo_nombre:
                        usuarios[num - 1] = nuevo_nombre
                        cambiar = True
                        print("---------------------------------")
                        print("*********************************")
                        print("      MODIFICANDO USUARIO...")
                        print("---------------------------------")
                        print("  ¡USUARIO MODIFICADO CON ÉXITO,")
                        print("      GRACIAS POR CONFIAR EN")
                        print("         CODELENGUAGEES!")
                        print("*********************************")
                        print("---------------------------------")
                        print(f" Usuario actualizado: {original} → {nuevo_nombre}")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Entrada inválida. Debe ser un número.")

        elif opcion == "3":
            if cambiar:
                guardar_usuarios(usuarios)
                guardar = True
                cambiar = False
                print("Cambios guardados correctamente.")
            else:
                print("No hay cambios por guardar.")

        elif opcion == "4":
            print("\nGracias por usar el sistema de modificación de usuarios.")
            print("Usuario actualizado con éxito en CodelenguageES 🧠✨")
            print("¡Tu código deja huella! 🧾")
            print("--------------------------------------")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
        print()

# Ejecutar el programa
mostrar_menu()