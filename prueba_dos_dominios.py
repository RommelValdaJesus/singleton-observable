from singleton_observable import SingletonObservable


class GestorPrestamos(SingletonObservable):
    def __init__(self):
        if not hasattr(self, "prestamos"):
            self.prestamos = []

    def registrar(self, prestamo):
        self.prestamos.append(prestamo)
        self.notificar(prestamo)


class GestorVentas(SingletonObservable):
    def __init__(self):
        if not hasattr(self, "ventas"):
            self.ventas = []

    def registrar(self, venta):
        self.ventas.append(venta)
        self.notificar(venta)


class GestorVuelos(SingletonObservable):
    def __init__(self):
        if not hasattr(self, "vuelos"):
            self.vuelos = []

    def registrar(self, vuelo):
        self.vuelos.append(vuelo)
        self.notificar(vuelo)

class GestorJoyas(SingletonObservable):
    def __init__(self):
        if not hasattr(self, "joyas"):
            self.joyas = []

    def registrar(self, joya):
        self.joyas.append(joya)
        self.notificar(joya)

gestor_biblioteca = GestorPrestamos()
gestor_jugueteria = GestorVentas()
gestor_aerolinea = GestorVuelos()
gestor_joyeria = GestorJoyas()

otro_gestor_biblioteca = GestorPrestamos()
print("¿Mismo gestor de biblioteca?", gestor_biblioteca is otro_gestor_biblioteca)
print("¿Biblioteca y juguetería son gestores distintos?", gestor_biblioteca is not  gestor_jugueteria)
print("¿Aerolínea y joyería son gestores distintos?", gestor_aerolinea is not gestor_joyeria)
print("¿Biblioteca y aerolínea son gestores distintos?", gestor_biblioteca is not gestor_aerolinea)
