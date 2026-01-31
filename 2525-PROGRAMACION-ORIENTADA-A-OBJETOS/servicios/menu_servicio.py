import os

class MenuService:
    # Constructor que recibe las dependencias necesarias
    # Inyeccion de dependencias: ArchivoService y EjecucionService
    def __init__(self, archivo_service, ejecucion_service):
        self.archivo_service = archivo_service
        self.ejecucion_service = ejecucion_service

    # Metodo principal para iniciar la aplicacion
    def iniciar(self):
        self.mostrar_menu_principal()

    # Muestra el menu de nivel superior (Unidades)
    def mostrar_menu_principal(self):
        while True:
            print("\n--- Menu Principal ---")
            
            # Utiliza el servicio de archivos para obtener las carpetas
            unidades = self.archivo_service.listar_directorios()
            
            # Filtra carpetas de sistema o configuracion
            unidades = [u for u in unidades if u not in ['modelos', 'servicios', '__pycache__', '.git']]

            for i, unidad in enumerate(unidades, start=1):
                print(f"{i} - {unidad}")
            print("0 - Salir")

            opcion = input("Seleccione una opcion: ")

            if opcion == '0':
                print("Finalizando programa.")
                break
            elif opcion.isdigit():
                idx = int(opcion) - 1
                if 0 <= idx < len(unidades):
                    # Navega al siguiente nivel (Subcarpetas)
                    self.mostrar_submenu(unidades[idx])
                else:
                    print("Opcion fuera de rango.")
            else:
                print("Entrada no valida.")

    # Muestra el submenú (Subcarpetas dentro de una Unidad)
    def mostrar_submenu(self, ruta_unidad):
        while True:
            subcarpetas = self.archivo_service.listar_directorios(ruta_unidad)
            
            print(f"\n--- Submenu: {ruta_unidad} ---")
            for i, carpeta in enumerate(subcarpetas, start=1):
                print(f"{i} - {carpeta}")
            print("0 - Regresar")

            opcion = input("Seleccione una subcarpeta: ")
            
            if opcion == '0':
                break
            elif opcion.isdigit():
                idx = int(opcion) - 1
                if 0 <= idx < len(subcarpetas):
                    # Construye la ruta relativa y navega a los scripts
                    nueva_ruta = os.path.join(ruta_unidad, subcarpetas[idx])
                    self.mostrar_scripts(nueva_ruta)
                else:
                    print("Opcion fuera de rango.")

    # Muestra la lista de scripts .py disponibles
    def mostrar_scripts(self, ruta_base):
        scripts = self.archivo_service.listar_scripts(ruta_base)

        while True:
            print(f"\n--- Scripts en: {ruta_base} ---")
            for i, script in enumerate(scripts, start=1):
                print(f"{i} - {script.nombre}")
            print("0 - Regresar")
            print("9 - Volver al inicio")

            opcion = input("Seleccione un script: ")

            if opcion == '0':
                break
            if opcion == '9':
                self.mostrar_menu_principal()
                return

            if opcion.isdigit():
                idx = int(opcion) - 1
                if 0 <= idx < len(scripts):
                    # Gestiona la visualizacion y ejecucion del script seleccionado
                    self.gestionar_script(scripts[idx])
                else:
                    print("Opcion fuera de rango.")

    # Muestra el codigo y solicita confirmacion para ejecutar
    def gestionar_script(self, script):
        codigo = self.archivo_service.leer_archivo(script.ruta)
        print(f"\n--- Codigo: {script.nombre} ---\n")
        print(codigo)
        print("-" * 30)

        confirmacion = input("¿Ejecutar script? (1: Si, 0: No): ")
        if confirmacion == '1':
            self.ejecucion_service.ejecutar_script(script.ruta)