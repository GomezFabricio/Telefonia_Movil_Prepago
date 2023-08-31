from classTiempo import Tiempo
import datetime 

#Nota: Agregar métodos set para dia, mes y año individualmente
class Fecha(Tiempo):
    def __init__(self, dia = 1, mes = 1, anio = 1900):
        super().__init__(dia, mes, anio)
    
    def getDia(self):
        return self.__dia

    def getMes(self):
        return self.__mes
    
    def getAnio(self):
        return self.__anio
        
    def incrementarFecha(self, numeroDias):
        self.__dia += numeroDias

    def imprimirFecha(self):
        nombreMes = self.mesLetra()
        mensajeFecha = f"{self.__dia} de {nombreMes} del {self.__anio}"
        return mensajeFecha

    def mesLetra(self):
        #Guardo los meses del año en una lista
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        nombre_mes = meses[self.__mes - 1]
        return nombre_mes

    def obtenerFechaActual(self):
        fecha_actual = datetime.datetime.now()
        self.__dia = fecha_actual.day
        self.__mes = fecha_actual.month
        self.__anio = fecha_actual.year


