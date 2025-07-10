"""
Creador:Angel A. Lopez C.
Fecha:4/07/2025
Version: 1.0
Descripcion:Crear un menu para agregar usuarios a la base de datos o bien iniciar sesion con los usuarios ya existentes.
"""

import os

ARCHIVO = "usuarios.txt"

#  Limpieza de pantalla
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

# 📥 Cargar usuarios desde el archivo
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

#  Guardar usuarios en el archivo
def guardar_usuarios(nombre_archivo, usuarios, contrasenas):
    with open(nombre_archivo, "w") as archivo:
        for i in range(len(usuarios)):
            archivo.write(f"{usuarios[i]},{contrasenas[i]}\n")

#  Menú de modificación
def menu_modificar_usuarios():
    usuarios, contrasenas = cargar_usuarios(ARCHIVO)
    limpiar_pantalla()
    while True:
        print(" MENÚ DE MODIFICACIÓN DE USUARIOS")
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. {usuario}")
        try:
            num = int(input(f"\nSeleccione número de usuario a modificar (1 - {len(usuarios)}), 0 para salir: "))
            if num == 0:
                break
            elif 1 <= num <= len(usuarios):
                original = usuarios[num - 1]
                print(f"\nUsuario: {original}")
                print("Seleccione nuevo rol:")
                print("1. Desarrollador")
                print("2. Colaborador")
                print("3. Usuario Plus")
                sub = input("Opción: ")
                roles = {"1": "Desarrollador", "2": "Colaborador", "3": "Usuario Plus"}
                if sub in roles:
                    for rol in roles.values():
                        original = original.replace(f" ({rol})", "")
                    nuevo_nombre = f"{original} ({roles[sub]})"
                    usuarios[num - 1] = nuevo_nombre
                    guardar_usuarios(ARCHIVO, usuarios, contrasenas)
                    print(f"✅ Usuario actualizado: {nuevo_nombre}")
                else:
                    print(" Rol inválido.")
            else:
                print(" Número fuera de rango.")
        except ValueError:
            print(" Entrada no válida.")
        input("\nPresione Enter para continuar...")
        limpiar_pantalla()

# 🗑️ Menú de eliminación
def menu_eliminar_usuarios():
    usuarios, contrasenas = cargar_usuarios(ARCHIVO)
    limpiar_pantalla()
    while True:
        print("🗑️ MENÚ DE ELIMINACIÓN DE USUARIOS")
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. {usuario}")
        elim_usuario = input("\nIngrese el nombre del usuario a eliminar (o 'salir' para terminar): ")
        if elim_usuario.lower() == "salir":
            break
        if elim_usuario in usuarios:
            idx = usuarios.index(elim_usuario)
            confirm = input(f"¿Confirmar eliminación de '{elim_usuario}'? (s/n): ")
            if confirm.lower() == "s":
                usuarios.pop(idx)
                contrasenas.pop(idx)
                guardar_usuarios(ARCHIVO, usuarios, contrasenas)
                print(" Usuario eliminado con éxito.")
            else:
                print(" Eliminación cancelada.")
        else:
            print( "Usuario no encontrado.")
        input("\nPresione Enter para continuar...")
        limpiar_pantalla()

#  Acceso especial
def administrar_sistema():
    while True:
        limpiar_pantalla()
        print(" MODO ADMINISTRADOR")
        print("1. Modificar usuarios")
        print("2. Eliminar usuarios")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_modificar_usuarios()
        elif opcion == "2":
            menu_eliminar_usuarios()
        elif opcion == "3":
            break
        else:
            print(" Opción no válida.")
            input("Presione Enter para continuar...")

#  Menú principal
def inicializar_archivo():
    if not os.path.exists(ARCHIVO):
        usuarios_iniciales = ["Ana", "Luis", "María", "Carlos", "patata"]
        claves_iniciales = ["1234", "abcd", "clave01", "password", "caliente"]
        guardar_usuarios(ARCHIVO, usuarios_iniciales, claves_iniciales)
def menu_usuarios():
    def menu_usuarios():
     inicializar_archivo()
    usuarios, contrasenas = cargar_usuarios(ARCHIVO)
    usuarios, contrasenas = cargar_usuarios(ARCHIVO)
    agregar_usuario = False

    while True:
        limpiar_pantalla()
        print(" MENÚ PRINCIPAL")
        print("1. Iniciar sesión")
        print("2. Agregar nuevo usuario")
        print("3. Guardar usuarios")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuariio = input("Usuario: ")
            pasword = input("Contraseña: ")

            if usuariio == "patata" and pasword == "caliente":
                administrar_sistema()
            elif usuariio in usuarios and contrasenas[usuarios.index(usuariio)] == pasword:
                print("Usuario verificado.")
            else:
                print(" Usuario o contraseña incorrectos.")
            input("Presione Enter para continuar...")

        elif opcion == "2":
            nuevo_usuario = input("Nuevo usuario: ")
            nueva_clave = input("Nueva contraseña: ")
            if nuevo_usuario not in usuarios:
                usuarios.append(nuevo_usuario)
                contrasenas.append(nueva_clave)
                agregar_usuario = True
                print(" Usuario agregado.")
            else:
                print(" El usuario ya existe.")
            input("Presione Enter para continuar...")

        elif opcion == "3":
            if agregar_usuario:
                guardar_usuarios(ARCHIVO, usuarios, contrasenas)
                agregar_usuario = False
                print(" Cambios guardados.")
            else:
                print("No hay nuevos usuarios.")
            input("Presione Enter para continuar...")

        elif opcion == "4":
            print(" Cerrando sistema...")
            break
        else:
            print(" Opción inválida.")
            input("Presione Enter para continuar...")

#  Ejecutar
menu_usuarios()