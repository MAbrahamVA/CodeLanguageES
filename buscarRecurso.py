"""
Creador: Moises A. Valle A.
Fecha: 9/07/2025
Version: 1.0
Descripcion: Permite a los usuarios buscar los recursos en base a palabra clave y filtros opcionales.
"""

# Definimos la clase que permite buscar recursos
class buscarRecurso:    

    # Método para buscar recursos por texto, con filtros opcionales por tipo y usuario
    def buscar_recursos(self, texto_busqueda, filtro_tipo=None, filtro_usuario_id=None):
        
        # Convierte el texto de búsqueda a minúsculas para hacer una comparación más flexible
        texto_busqueda = texto_busqueda.lower()

        # Lista que filtra los recursos según:
        # - Si el texto está en el título, tipo, descripción o URL
        # - Si el tipo del recurso coincide con el filtro (si se ha especificado)
        # - Si el ID del usuario coincide con el filtro (si se ha especificado)
        resultados = [
            r for r in self.recursos
            if (
                texto_busqueda in r["titulo"].lower()
                or texto_busqueda in r["tipo"].lower()
                or texto_busqueda in r["descripcion"].lower()
                or texto_busqueda in r["url"].lower()
            )
            and (filtro_tipo is None or r["tipo"].lower() == filtro_tipo.lower())
            and (filtro_usuario_id is None or r["usuario_id"] == filtro_usuario_id)
        ]

        # Verifica si hay resultados y los muestra en consola
        if resultados:
            print(f"\n Resultados de búsqueda para: '{texto_busqueda}'")
            for r in resultados:
                # Muestra los detalles relevantes de cada recurso encontrado
                print(f"- {r['titulo']} ({r['tipo']}) | Usuario ID {r['usuario_id']} | {r['fecha']}")
        else:
            # Si no se encontraron resultados, imprime un mensaje indicando eso
            print(f"\n No se encontraron recursos que coincidan con: '{texto_busqueda}'")

