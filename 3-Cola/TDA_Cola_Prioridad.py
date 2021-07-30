class Cola():
    def __init__(self):
        self.__elementos = []
        self.__prioridad = []

    def arribo(self, dato, prioridad):
        self.__elementos.append(dato)

    def atencion(self):
        return (self.__elementos.pop(0))

    def cola_vacia(self):
        return len(self.__elementos) == 0

    def en_frente(self):
        return (self.__elementos[0])

    def move_end(self):
        dato = self.atencion()
        self.arribo(dato)
        return (dato)

    def tamanio(self):
        return len(self.__elementos)

    def aplicar_prioridad_ascendente(self):
        self.__elementos.sort()
        self.__prioridad.sort()

    def aplicar_prioridad_descendente(self):
        pass
