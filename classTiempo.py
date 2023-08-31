from classValidaciones import Validaciones

class Tiempo:
    def __init__(self, hora = 0, minutos = 0, segundos = 0, dia = 1, mes = 1, anio = 1900):
        self.validacion = Validaciones()
        self.hora = self.validacion.validarHora(hora)
        self.minutos = self.validacion.validarMinutos(minutos)
        self.segundos = self.validacion.validarSegundos(segundos)
        self.__dia = self.validacion.validarDia(dia)
        self.__mes = self.validacion.validarMes(mes)
        self.__anio = self.validacion.validarAnio(anio)

    def __setFecha(self, dia, mes, anio):
        self.__dia = self.validacion.validarDia(dia)
        self.__mes = self.validacion.validarMes(mes)
        self.__anio = self.validacion.validarAnio(anio)
    
    def __setHorario (self, hora, minutos, segundos):
        self.__hora = self.validacion.validarHora(hora)
        self.__minutos = self.validacion.validarMinutos(minutos)
        self.__segundos = self.validacion.validarSegundos(segundos)