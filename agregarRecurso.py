"""
Creador: Moises A. Valle A.
Fecha: 9/07/2025
Version: 1.0
Descripcion: Permite agregar recursos vinculados a un usuario existente.
"""

from datetime import datetime  # Importa la clase datetime para obtener la fecha y hora actuales

# Definimos la clase para manejar usuarios y recursos en memoria
class agregarRecurso:
    def __init__(self):
        self.usuarios = []   # Lista para guardar usuarios registrados
        self.recursos = []   # Lista para guardar recursos agregados

    # Método para registrar un nuevo usuario
    def registrar_usuario(self, nombre, correo):
        usuario = {
            "id": len(self.usuarios) + 1,     # Genera un ID único basado en la cantidad actual de usuarios
            "nombre": nombre,                 # Guarda el nombre del usuario
            "correo": correo                  # Guarda el correo del usuario
        }
        self.usuarios.append(usuario)         # Agrega el nuevo usuario a la lista
        print(f"Usuario registrado: {usuario['nombre']} (ID {usuario['id']})")

    # Método para verificar si un usuario existe por su ID
    def usuario_valido(self, usuario_id):
        # Busca si hay algún usuario con el ID dado y retorna True/False
        return any(u["id"] == usuario_id for u in self.usuarios)

    # Método para agregar un recurso vinculado a un usuario registrado
    def agregar_recurso(self, titulo, tipo, descripcion, url, usuario_id):
        if not self.usuario_valido(usuario_id):
            print("Usuario no registrado.")  # Mensaje si el usuario no existe
            return

        recurso = {
            "id": len(self.recursos) + 1,            # Genera un ID único para el recurso
            "titulo": titulo,                        # Título del recurso
            "tipo": tipo,                            # Tipo (ej. artículo, video, herramienta)
            "descripcion": descripcion,              # Descripción opcional
            "url": url,                              # Enlace si aplica
            "usuario_id": usuario_id,                # ID del usuario que lo registró
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Fecha y hora actual
        }
        self.recursos.append(recurso)               # Añade el recurso a la lista
        print(f"Recurso agregado: {recurso['titulo']}")

    # Método para mostrar todos los recursos guardados
    def listar_recursos(self):
        print("\n Recursos disponibles:")
        for r in self.recursos:
            print(f"- {r['titulo']} ({r['tipo']}) por usuario ID {r['usuario_id']} en {r['fecha']}")
