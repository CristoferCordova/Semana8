import os
from servicios.archivo_servicios import ArchivoService
from servicios.ejecucion_servicio import EjecucionService
from servicios.menu_servicio import MenuService

# Bloque principal de ejecucion
if __name__ == "__main__":
    # 1. Configuracion de la ruta base del proyecto
    # Se obtiene la ruta absoluta del directorio actual
    ruta_proyecto = os.path.dirname(os.path.abspath(__file__))

    # 2. Creacion de objetos de servicio (Instanciacion)
    # Servicio para manejar operaciones de archivos
    servicio_archivos = ArchivoService(ruta_proyecto)
    # Servicio para manejar la ejecucion de procesos
    servicio_ejecucion = EjecucionService()

    # 3. Inyeccion de dependencias
    # Se crea el servicio de menu inyectando los servicios necesarios
    menu = MenuService(servicio_archivos, servicio_ejecucion)

    # 4. Inicio del flujo de la aplicacion
    menu.iniciar()