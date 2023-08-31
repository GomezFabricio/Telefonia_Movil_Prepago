from classTiempo import Tiempo
import datetime

class Hora(Tiempo):
    def __init__(self, hora = 0, minutos = 0, segundos = 0, consumo = 0):
        super().__init__(hora, minutos, segundos)
        self.consumo = {"Horas": 0, "Minutos": 0, "Segundos": 0}

    def getHoraProp (self):
        return self._Tiempo__hora

    def getMinutos (self):
        return self._Tiempo__minutos

    def getSegundos(self):
        return self._Tiempo__segundos

    def __setHora (self, hora, minutos, segundos):
        self.__setHorario (hora, minutos, segundos)

    def __setMinutos (self, minutos):
        self.__setHorario (self.hora, minutos, self.__segundos)

    def __setSegundos (self, segundos):
        self.__setHorario (self.__hora, self.__minutos, segundos)

    def showConsumo (self):
        return f"Horas: {self.consumo['Horas']} | Minutos: {self.consumo['Minutos']} | Segundos: {self.consumo['Segundos']}"

    # Sumamos la duracion de la llamada al consumo actual de la tarjeta prepaga
    def sumarDuracion(self, duracionSegundos):
        consumoAcumuladoEnSegundos = (self.consumo['Horas'] * 3600) + (self.consumo['Minutos'] * 60) + (self.consumo['Segundos']); #Obtenemos el total acumulado de consumo en segundos
        totalConsumo = consumoAcumuladoEnSegundos + duracionSegundos
    
        consumoHoras = totalConsumo // 3600 #Convertimos los segundos en horas y las guardamos
        consumoMinutos = (totalConsumo % 3600) // 60 #Calculamos el residuo de la conversion segundos a horas y lo dividimos sobre 60 para guardar los minutos
        consumoSegundos = totalConsumo % 60 #Calculamos el residuo de la conversion segundos a minutos y guardamos los segundos

        self.consumo['Horas'] = consumoHoras;
        self.consumo['Minutos'] = consumoMinutos;
        self.consumo['Segundos'] = consumoSegundos;

    def obtenerHoraActual(self):
        getHoraActual = datetime.datetime.now().time()
        horaActualStr = getHoraActual.strftime("%H:%M:%S")
        return horaActualStr

