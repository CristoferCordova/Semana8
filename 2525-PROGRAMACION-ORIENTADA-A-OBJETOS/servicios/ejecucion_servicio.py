import os
import sys  # Importamos sys para obtener la ruta del interprete actual
import subprocess

class EjecucionService:
    # Ejecuta un script de Python en una nueva terminal
    # Determina el sistema operativo para usar el comando adecuado
    def ejecutar_script(self, ruta_script):
        try:
            # sys.executable contiene la ruta absoluta al python.exe actual
            # Esto evita errores si el comando 'python' no esta en el PATH
            ruta_python = sys.executable

            if os.name == 'nt':  # Configuracion para Windows
                # Usamos ruta_python en lugar de 'python'
                subprocess.Popen(['cmd', '/k', ruta_python, ruta_script])
            else:  # Configuracion para sistemas basados en Unix (Linux/Mac)
                subprocess.Popen(['xterm', '-hold', '-e', ruta_python, ruta_script])
        except Exception as e:
            print(f"Error de ejecucion: {e}")