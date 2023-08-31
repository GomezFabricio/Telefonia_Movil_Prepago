from classCuentaCorriente import CuentaCorriente
from classDNI import DNI
from classFecha import Fecha
from classHora import Hora
from classTarjetaPrepago import TarjetaPrepago
from classValidaciones import Validaciones

validacion = Validaciones()

print("-------------------------------------------------------------------")
print("¡Bienvenido a nuestra aplicación de telefonía móvil prepago!")
print("-------------------------------------------------------------------")

respuesta = validacion.validarContinuar("¿Desea abrir una cuenta? (S/N): ")

if respuesta == "s":
    # Aquí puedes pedir al usuario que ingrese los datos necesarios para crear una cuenta
    print("-------------------------------------------------------------------")
    nombre = validacion.validarNombres("Ingrese su nombre: ")
    apellido = validacion.validarNombres("Ingrese su apellido: ")
    direccion = validacion.validarString("Ingrese su dirección: ")
    telefono = validacion.validarTelefono("Ingrese su número de teléfono: ")
    nif_numero = validacion.validarDNI("Ingrese su número de NIF: ")

    # Crea una instancia de DNI
    nif = DNI(nif_numero)

    # Crea una instancia de CuentaCorriente
    cuentaCorriente1 = CuentaCorriente(nombre, apellido, direccion, telefono, nif)

    # Crea una instancia de TarjetaPrepago
    tarjetaPrepago1 = TarjetaPrepago(telefono, nif)

    print("¡Cuenta creada exitosamente!")   

    while True:
        print("-------------------------------------------------------------------")
        print("MENU DE OPCIONES")
        print("1 - Recargar saldo en Tarjeta Prepago")
        print("2 - Enviar Mensaje/s")
        print("3 - Realizar Llamada")
        print("4 - Consultar Consumo")
        print("5 - Recargar Cartera Virtual")
        print("6 - Consultar Cartera Virtual")
        print("7 - Consultar Tarjeta Prepago")
        print("8 - Historial de Recarga de Saldo")
        print("9 - Salir")
        respuesta = validacion.validarEntero("Respuesta: ")
        print("-------------------------------------------------------------------")   

        if respuesta == 1:
            saldoCartera = cuentaCorriente1.getSaldo()

            if saldoCartera <= 0.0:
                print("No posee dinero disponible para cargar su tarjeta prepaga");
                continuar = validacion.validarContinuar("\n¿Desea Continuar? (S/N):")
                print("-------------------------------------------------------------------")   
            else:
                while True:
                    print(f"Monto disponible en Cartera para Operar: ${saldoCartera}")
                    cantidad = validacion.validarEntero("Ingrese la cantidad de saldo que desea cargar: ");
                    saldoCartera -= cantidad
                    if cantidad > 0 and cantidad <= saldoCartera:
                        tarjetaPrepago1.ingresarSaldo(cantidad)
                        cuentaCorriente1.setSaldo(saldoCartera)
                        print("\nEl saldo de su tarjeta prepaga se ha actualizado correctamente")
                        print(f"Se ha descontado del monto de su Cartera, la cantidad de ${cantidad}")
                        continuar = validacion.validarContinuar("\n¿Desea Continuar? (S/N): ")
                        break
                    else:
                        print("Ingrese un monto válido")
                        print("-------------------------------------------------------------------")    


        elif respuesta == 2:
            cantidad_mensajes = validacion.validarEntero("Ingrese la cantidad de mensajes a enviar: ")
            if tarjetaPrepago1.enviarMensaje(cantidad_mensajes):
                print("Mensaje(s) enviado(s) exitosamente.")
            else:
                print("No tienes suficiente saldo para enviar mensaje(s).") 
            continuar = validacion.validarContinuar("\n¿Desea Continuar? (S/N): ")   

        elif respuesta == 3:
            duracion_segundos = validacion.validarEntero("Ingrese la duración de la llamada en segundos: ")
            if tarjetaPrepago1.realizarLlamada(duracion_segundos):
                print("Llamada realizada exitosamente.")
            else:
                print("No tienes suficiente saldo para realizar la llamada.")    
            continuar = validacion.validarContinuar("\n¿Desea Continuar? (S/N): ")

        elif respuesta == 4:
            print(f"Consumo: {tarjetaPrepago1.consumo.showConsumo()}")
            continuar = validacion.validarContinuar("\n¿Desea Continuar? (S/N): ")

        elif respuesta == 5:

            cantidad = validacion.validarEntero("Ingrese la cantidad de dinero que desea ingresar a su Cartera: ")
            ingreso = cuentaCorriente1.ingresarDinero(cantidad)
            
            if ingreso:
                print("El ingreso de dinero se ha realizado satisfactoriamente.")
            else:
                print("El ingreso de dinero no se ha realizado satisfactoriamente.")
            continuar = validacion.validarContinuar("\n¿Desea Continuar? (S/N): ")

        elif respuesta == 6:
            cuentaCorriente1.consultarCuenta()
            continuar = validacion.validarContinuar("\n¿Desea Continuar? (S/N): ")

        elif respuesta == 7:
            tarjetaPrepago1.consultarTarjeta()
            continuar = validacion.validarContinuar("\n¿Desea Continuar? (S/N): ")

        elif respuesta == 8:
            tarjetaPrepago1.consultarRecargas()
            continuar = validacion.validarContinuar("\n¿Desea Continuar? (S/N): ")

        elif respuesta == 9:
            print("¡Gracias por utilizar nuestra aplicación de telefonía móvil prepago!")
            break 
        else:
            print("-------------------------------------------------------------------")
            print("Opción no válida. Por favor, ingrese un número de opción válido.")
            print("-------------------------------------------------------------------")


