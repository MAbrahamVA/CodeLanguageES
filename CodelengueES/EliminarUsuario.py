"""
Creador:Angel A. Lopez C.
Fecha:4/07/2025
Version: 1.0
Descripcion:Gestionar la eliminacion de datos de usuarios en el programa de CodelenguageES.
"""
def cargar_usuarios(nombre_archivo):
    usuarios = []
    contrasenas = []
    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                if len(partes) == 2:
                    usuarios.append(partes[0])
                    contrasenas.append(partes[1])
    except FileNotFoundError:
        pass  
    return usuarios, contrasenas

def guardar_usuarios(nombre_archivo, usuarios, contrasenas):
    with open(nombre_archivo, "w") as archivo:
        for i in range(len(usuarios)):
            archivo.write(f"{usuarios[i]},{contrasenas[i]}\n")

def menu_eliminar_usuarios():
    archivo_usuarios = "usuarios.txt"
    usuarios, contrasenas = cargar_usuarios(archivo_usuarios)

    while True:
        print("--------- MENÚ DE ELIMINACIÓN DE USUARIOS ---------")
        print("1. Ver usuarios")
        print("2. Eliminar un usuario")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                print("Usuarios registrados:")
                for i, nombre in enumerate(usuarios, start=1):
                    print(f"{i}. {nombre}")

        elif opcion == "2":
            if not usuarios:
                print("No hay usuarios que eliminar.")
            else:
                elim_usuario = input("Ingrese el nombre del usuario que desea eliminar: ")
                encontrado = False
                for i in range(len(usuarios)):
                    if usuarios[i] == elim_usuario:
                        borrar_datos = usuarios[i]
                        elim_datos = contrasenas[i]
                        usuarios.pop(i)
                        contrasenas.pop(i)
                        encontrado = True
                        break

                if encontrado:
                    guardar_usuarios(archivo_usuarios, usuarios, contrasenas)
                    print("---------------------------------")
                    print("*********************************")
                    print("      ELIMINANDO USUARIO...")
                    print("---------------------------------")
                    print("  ¡USUARIO ELIMINADO CON ÉXITO,")
                    print("      GRACIAS POR CONFIAR EN")
                    print("         CODELENGUAGEES!")
                    print("*********************************")
                    print("---------------------------------")
                    print(f"Usuario eliminado: {borrar_datos}")
                else:
                    print("Usuario no encontrado.")

        elif opcion == "3":
            print("")
            print("Gracias por usar el sistema de eliminación de usuarios.")
            print("Sistema desarrollado en CodelenguageES. 🧠💻")
            print("----------------------------------------------")
            break

        else:
            print("Opción inválida. Intente nuevamente.")
        print()


menu_eliminar_usuarios()