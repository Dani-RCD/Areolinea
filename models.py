class Vuelo:
    def __init__(self, id_vuelo, origen, destino, fecha, precio):
        self.id_vuelo = id_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.precio = precio

class Reserva:
    def __init__(self, id_reserva, id_vuelo, nombre, cantidad):
        self.id_reserva = id_reserva
        self.id_vuelo = id_vuelo
        self.nombre = nombre
        self.cantidad = cantidad

vuelos = []
reservas = []
