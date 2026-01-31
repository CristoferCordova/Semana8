class Script:
    # Constructor de la clase Script
    # Inicializa los atributos nombre y ruta
    def __init__(self, nombre, ruta):
        self.nombre = nombre
        self.ruta = ruta

    # Representacion en cadena del objeto
    # Devuelve el nombre del script cuando se imprime el objeto
    def __str__(self):
        return self.nombre
