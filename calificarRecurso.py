"""
Creador: Moises A. Valle A.
Fecha: 9/07/2025
Version: 1.0
Descripcion: Permite a los usuarios agregar una califación con comentario.
"""

from datetime import datetime  # Importamos datetime para registrar la fecha de cada calificación

# Definimos la clase que se encargará de las calificaciones
class CalificarRecurso:
    # Se recibe las listas de recursos y usuarios
    def __init__(self, recursos, usuarios):
        self.recursos = recursos      # Lista de recursos disponibles
        self.usuarios = usuarios      # Lista de usuarios registrados

    # Función para calificar un recurso
    def calificar_recurso(self, recurso_id, usuario_id, puntuacion, comentario=""):
        # Verifica que la puntuación esté entre 1 y 5
        if not (1 <= puntuacion <= 5):
            print(" La puntuación debe estar entre 1 y 5.")  # Mensaje de advertencia
            return

        # Busca al usuario por ID para verificar que esté registrado
        usuario = next((u for u in self.usuarios if u["id"] == usuario_id), None)
        if not usuario:
            print(f" Usuario con ID {usuario_id} no encontrado.")  # Si no existe, se muestra error
            return

        # Busca el recurso por ID
        recurso = next((r for r in self.recursos if r["id"] == recurso_id), None)
        if not recurso:
            print(f" Recurso con ID {recurso_id} no encontrado.")  # Si no existe, se muestra error
            return

        # Si el recurso no tiene aún calificaciones, se inicializa la lista
        if "calificaciones" not in recurso:
            recurso["calificaciones"] = []  # Se crea el campo como lista vacía

        # Se agrega una nueva calificación al recurso
        recurso["calificaciones"].append({
            "usuario": usuario["nombre"],                           # Nombre del usuario que califica
            "puntuacion": puntuacion,                               # Número entre 1 y 5
            "comentario": comentario,                               # Texto opcional del usuario
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")   # Fecha de la calificación
        })

        # Se confirma en consola que la operación fue exitosa
        print(f"{usuario['nombre']}' calificó el recurso '{recurso['titulo']}' con {puntuacion}/5.")