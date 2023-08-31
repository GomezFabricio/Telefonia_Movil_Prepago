import re

class Validaciones():

    @staticmethod
    def validarNombres(mensaje):
        while True:
            nombre = input(mensaje)
            if re.match("^[a-zA-Z\s]+$", nombre):  # Verificar si el nombre contiene solo letras y espacios
                return nombre
            else:
                print("Por favor, ingrese un nombre válido sin caracteres especiales.")
    
    # Método de clase público para validar y obtener un valor entero a partir de la entrada del usuario.
    # El mensaje se muestra al usuario para indicar qué tipo de entrada se espera.
    @staticmethod
    def validarEntero(mensaje):
        while True:
            try:
                numero = int(input(mensaje))
                return numero
            except ValueError:
                print("Por favor, ingrese un valor entero válido.")

    # Método de clase público para validar y obtener una cadena no vacía a partir de la entrada del usuario.
    # El mensaje en print muestra al usuario para indicar qué tipo de entrada se espera.
    @staticmethod
    def validarString(mensaje):
        while True:
            entrada = input(mensaje)
            if entrada.strip():  # Verificar si la cadena no está vacía
                return entrada
            else:
                print("Por favor, ingrese un valor válido.")

    # Método de clase público para validar y obtener un número de teléfono válido con 10 dígitos.
    # El mensaje en print muestra al usuario para indicar qué tipo de entrada se espera.
    @staticmethod
    def validarTelefono(mensaje):
        while True:
            telefono = input(mensaje)
            if telefono.isdigit() and len(telefono) == 10:
                return telefono
            else:
                print("Por favor, ingrese un número de teléfono válido con 10 dígitos.")

    # Método de clase público para validar y obtener un número de DNI válido con 8 dígitos.
    # El mensaje en print muestra al usuario para indicar qué tipo de entrada se espera.
    @staticmethod
    def validarDNI(mensaje):
        while True:
            dni = input(mensaje)
            if dni.isdigit() and len(dni) == 8:
                return dni
            else:
                print("Por favor, ingrese un número de DNI válido con 8 dígitos.")

    # Método de clase público para validar si el usuario desea continuar.
    # El mensaje en print muestra un mensaje de salida de la aplicación.
    @staticmethod
    def validarContinuar(mensaje):
        while True:
            entrada = input(mensaje).lower()
            if entrada == "s":
                return entrada
                break
            elif entrada == "n":
                print("¡Gracias por utilizar nuestra aplicación de telefonía móvil prepago!")
                exit()

    # ---------------------- Validaciones de la clase Fecha ---------------------- #
    @staticmethod
    def validarDia(dia):
        try:
            #verificamos que el dia se encuentre en el rango entre 1 y 31
            if 1 <= dia <= 31:
                return dia
            else: 
                raise ValueError("El Dia ingresado esta fuera de Rango!!")
        except ValueError:
                #Aqui mostramos el error del ValueError y reestablecemos el valor a 1
                print("El dia ingresado es invalido, se establecera a 1 automaticamente.")
                return 1

    @staticmethod
    def validarMes(mes):
        #Aplicamos la misma logica que en el bloque de Dia
        try: 
            if 1 <= mes <= 12:
                return mes
            else:
                raise ValueError("El Mes ingresado esta fuera de Rango!!")
        except ValueError:
                print("El mes ingresado es invalido, se establecera a 1 automaticamente. ")
                return 1

    @staticmethod
    def validarAnio(anio):
        try:
            if 1900 <= anio <= 3000:
                return anio
            else:
                raise ValueError("El anio ingresado esta fuera de Rango!!")
        except ValueError:
                print("El anio ingresado es invalido, se establecera a 1900 automaticamente. ")
                return 1900
                

    # ----------------------- Validaciones de la clase Hora ---------------------- #
    @staticmethod
    def validarHora(hora):
        return hora if 0 <= hora <= 24 else 0

    @staticmethod
    def validarMinutos(minutos):
        return minutos if 0 <= minutos <= 59 else 0

    @staticmethod
    def validarSegundos(segundos):
        return segundos if 0 <= segundos <= 59 else 0