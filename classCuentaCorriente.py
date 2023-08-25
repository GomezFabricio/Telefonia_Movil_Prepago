class CuentaCorriente:
    #Se procede a la creación de un constructor que inicialice los atributos de la cuenta corriente.
    def __init__(self, nombre, apellido, direccion, telefono, NIF, saldo = 0.0):
        self.__nombre = nombre;
        self.__apellido = apellido;
        self.__direccion = direccion;
        self.__telefono = telefono;
        self.__NIF = NIF;
        self.__saldo = saldo;

    #Creamos la funcion getNombre que retornara el nombre del titular de la cuenta.
    def getNombre (self):
        return self.__nombre;

    #Creamos la funcion setNombre para establecer el nombre del titular de la cuenta.
    def setNombre (self, nombre):
        self.__nombre = nombre;
    
    #Creamos la funcion getApellido que retornara el apellido del titular de la cuenta.
    def getApellido (self):
        return self.__apellido;

    #Creamos la funcion setNombre para establecer el apellido del titular de la cuenta.
    def setApellido (self, apellido):
        self.__apellido = apellido;

    #Retornamos la direccion del titular de la cuenta.
    def getDireccion (self):
        return self.__direccion;

    #Con esta funcion establecemos la direccion del titular de la cuenta.
    def setDireccion (self, direccion):
        self.__direccion = direccion;

    #Retornamos el numero del telefono del titular.
    def getTelefono (self):
        return self.__telefono;

    #Establecemos el numero telefonico del titular de la cuenta.
    def setTelefono (self, telefono):
        self.__telefono = telefono;
    
    #Retornamos el numero de identificacion fiscal del titular.
    def getNIF (self):
        return self.__NIF;
    
    #Establecemos un nuevo NIF para el titular de la cuenta.
    def setNIF (self, NIF):
        self.__NIF = NIF;

    # Método para obtener el saldo actual de la instancia.
    def getSaldo (self):
        return self.__saldo;

    # Método para establecer el saldo de la instancia a la cantidad especificada.
    def setSaldo (self, cantidad):
        self.__saldo = cantidad;

    # Metodo para retirar dinero de la cuenta
    def retirarDinero (self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad;
            return True
        else:
            return False
        
    # Metodo para agregar dinero a la cuenta
    def ingresarDinero (self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return True
        else:
            return False
        
    # Metodo para consultar datos de la cuenta
    def consultarCuenta (self):
        print ("\nNombre: ", self.__nombre);
        print ("Apellido: ", self.__apellido);
        print ("Direccion: ", self.__direccion);
        print ("Telefono: ", self.__telefono);
        print ("NIF numero: ", self.__NIF.numero);
        print ("Saldo: ", self.__saldo);

    # Metodo para consultar saldo negativo
    def saldoNegativo (self):
        if self.__saldo < 0:
            return True
        else:
            return False








