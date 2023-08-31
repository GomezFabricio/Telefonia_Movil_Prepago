from classDNI import DNI
from classHora import Hora
from classCuentaCorriente import CuentaCorriente
from classFecha import Fecha

# Constructor de la clase TarjetaPrepago.
# Inicializa las propiedades numeroTelefono, NIF, saldo y consumo.
class TarjetaPrepago:
    def __init__(self, numeroTelefono, NIF, saldo = 0):
        self.__numeroTelefono = numeroTelefono
        self.__NIF = NIF
        self.__saldo = saldo
        self.consumo = Hora(0, 0, 0)  # Inicializa el consumo con una instancia de Hora
        self.__recargas = []
    
    # Método público para obtener el número de teléfono.
    def getNumeroTelefono(self):
        return self.__numeroTelefono

    # Método público para establecer el número de teléfono.
    def setNumeroTelefono(self, numeroTelefono):
        self.__numeroTelefono = numeroTelefono

    # Método público para obtener el NIF.
    def getNIF(self):
        return self.__NIF

    # Método privado para establecer el NIF.
    def __setNIF(self, NIF):
        self.__NIF = NIF

    # Método público para obtener el saldo.
    def getSaldo(self):
        return self.__saldo

    # Método protegido para establecer el saldo.
    def _setSaldo(self, saldo):
        self.__saldo = saldo
    
    # Método público para ingresar saldo a la cuenta.
    def ingresarSaldo(self, cantidad):
        self.__saldo += cantidad;
        fecha = Fecha()
        fecha_actual = fecha.obtenerFechaActual()
        recarga = {"Monto": cantidad, "Fecha": fecha.imprimirFecha()}
        self.__recargas.append(recarga)

    def enviarMensaje(self, cantidad):
        # Resta 9 céntimos por mensaje al saldo
        costo_mensaje = 0.9 * cantidad
        if costo_mensaje <= self.__saldo:
            self.__saldo -= costo_mensaje
            return True
        else:
            return False

    # Método público para realizar una llamada.
    def realizarLlamada(self, duracion_segundos):
        # Resta saldo según costos de llamada y actualiza el consumo
        costo_establecimiento = 0.15
        costo_por_segundo = 0.1

        costo_llamada = (costo_establecimiento + costo_por_segundo) * duracion_segundos
        if costo_llamada <= self.__saldo:
            self.__saldo -= costo_llamada
            self.actualizarConsumoLlamada(duracion_segundos)
            return True
        else:
            return False

    # Método público para actualizar el consumo de llamada.
    def actualizarConsumoLlamada(self, duracion_segundos):
            self.consumo.sumarDuracion(duracion_segundos)

    # Método público para consultar y mostrar todos los datos de la tarjeta.
    def consultarTarjeta(self):
        print("Número de Teléfono:", self.__numeroTelefono)
        print("NIF:", self.__NIF.numero)
        print("Saldo:", self.__saldo)
        print("Consumo:", self.consumo.showConsumo())

    def consultarRecargas(self):
        print("Historial de recargas:")
        for unaRecarga in self.__recargas:
            print(f"Cantidad: {unaRecarga['Monto']} | Fecha: {unaRecarga['Fecha']}")


