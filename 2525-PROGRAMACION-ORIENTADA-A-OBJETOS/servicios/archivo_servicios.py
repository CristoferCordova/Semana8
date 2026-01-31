import os
from modelos.script_model import Script

class ArchivoService:
    # Inicializa el servicio con la ruta base del proyecto
    def __init__(self, ruta_raiz):
        self.ruta_raiz = ruta_raiz

    # Lista los directorios dentro de una ruta especifica
    # Retorna una lista de nombres de directorios
    def listar_directorios(self, ruta_relativa=""):
        ruta_completa = os.path.join(self.ruta_raiz, ruta_relativa)
        if not os.path.exists(ruta_completa):
            return []
        # Filtra solo los elementos que son directorios
        return [f.name for f in os.scandir(ruta_completa) if f.is_dir()]

    # Busca archivos .py en una ruta especifica
    # Retorna una lista de objetos Script (Modelo)
    def listar_scripts(self, ruta_relativa):
        ruta_completa = os.path.join(self.ruta_raiz, ruta_relativa)
        scripts = []
        if os.path.exists(ruta_completa):
            for f in os.scandir(ruta_completa):
                # Filtra archivos que terminan en .py
                if f.is_file() and f.name.endswith('.py'):
                    scripts.append(Script(f.name, f.path))
        return scripts

    # Lee el contenido de un archivo de texto
    # Retorna el contenido como string o un mensaje de error
    def leer_archivo(self, ruta_script):
        try:
            with open(ruta_script, 'r', encoding='utf-8') as archivo:
                return archivo.read()
        except Exception as e:
            return f"Error al leer archivo: {e}"