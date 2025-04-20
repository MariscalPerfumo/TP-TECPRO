from datetime import datetime, timedelta

class Ciudad:
    def __init__(self, codigo, nombre, provincia):
        self.codigo = codigo
        self.nombre = nombre
        self.provincia = provincia
    def verCodigo(self):
        cod = self.codigo
        return cod
    def verNombre(self):
        nom = self.nombre
        return nom
    def verProvincia(self):
        prov = self.provincia
        return prov
        
class Intinerario:
    def __init__(self, origen, destino, paradas):
        self.origen = origen
        self.destino = destino
        self.paradas = paradas
    def verOrigen(self):
        orig = self.origen
        return orig
    def verDestino(self):
        desti = self.destino          #Funciones que devulven los valores privados
        return desti
    def verParadas(self):
        para = self.paradas
        return para
    
        
class Unidad:
    def __init__(self, patente, asientos):
        self.patente = patente
        self.asientos = asientos
    def verAsientosLibres(self):
        libres = []
        for lib in self.asientos: #Para cada asiento
            if lib.verificarOcupacion(): #Si está libre, lo añade a la lista de asientos libres
                libres.append(lib)
        return libres
    def verAsientos(self):
        asientos = self.asientos
        return asientos

class Asiento:
    def __init__(self, numero):
        self.ocupado = False
        self.numero = numero
    def verificarOcupacion(self): #Devuelve el estado del asiento (libre u ocupado)
        esLibre = self.ocupado
        return esLibre
    def verNumeroAsiento(self): #Devuleve el numero de asiento
        num = self.numero 
        return num
    def cambiarEstadoAsiento(self): #Funcion que cambia el estado del asiento
        if self.ocupado == True:
            self.ocupado = False
        else:
            self.ocupado = True

class Servicio:
    def __init__(self, itinerario, unidad, fechaPartida, fechaLlegada, calidad, precio):
        self.itinerario = itinerario
        self.unidad = unidad
        self.fechaPartida = fechaPartida
        self.fechaLlegada = fechaLlegada
        self.precio = precio
    def verUnidad(self):
        uni = self.unidad
        return uni
    def verFechaPartida(self):
        fPartida = self.fechaPartida
        return fPartida
    def verFechaLlegada(self):
        fLlegada = self.fechaLlegada
        return fLlegada
    def verCalidad(self):
        cal = self.calidad
        return cal
    def verPrecio(self):
        costo = self.precio
        return costo
    
        
class Pasajero:
    def __init__(self, nombre, email, dni):
        self.nombre = nombre
        self.email = email
        self.dni = dni
        
class Reserva:
    def __init__(self, pasajero, servicio, asiento):
        self.pasajero = pasajero
        self.servicio = servicio
        self.asiento = asiento
        self.fechaHora = datetime.now()
    def expirado(self): # Funcion que me dice si ya pasaron los 30 minutos de la reserva
        expiro = False
        if(datetime.now() >= (self.fechaHora - timedelta(minutes=30))): #Si pasaron 30 minutos, la reserva caducó
            expiro = True
        return expiro

class Venta:
    def __init__(self, pasajero, servicio, asiento, medioPago):
        self.fechaHora = datetime.now()
        self.pasajero = pasajero
        self.servicio = servicio
        self.asiento = asiento
        self.medioPago = medioPago
        self.costo = servicio.verPrecio()
        
class MedioPago:
    def __init__(self):
        pass
    def validarPago(self):
        pass

class TarjetaDeCredito(MedioPago):
    def __init__(self, numero, dniTitular, nombre, fechaVencimiento):
        self.numero = numero
        self.dniTitular = dniTitular
        self.nombre = nombre
        self.fechaVencimiento = fechaVencimiento
    def validarPago(self):
        return True             #Simulacion de validacion

class MercadoPago(MedioPago):
    def __init__(self, celular, email):
        self.celular = celular
        self.email = email
        

class Uala(MedioPago):
    def __init__(self, email, nombreTitular):
        self.email = email
        self.nombreTitular = nombreTitular
    def validarPago(self):
        return True             #Simulacion de validacion    

class Argentur:
    def __init__(self):
        self.sistemaActivo = True
        self.listaServicios = []
        self.listaReservas = []
        self.listaVentas = []
        self.Unidades = []
    def agregarServicio(self, servicio):
        self.listaReservas.append(servicio)
    def reservarAsiento(self, pasajero, servicio, numAsiento, reserva):
        asiento = next((a for a in servicio.verUnidad().verAsientos() if a.verNumero() == numAsiento), None)
        if asiento and not asiento.VerificarOcupacion():
            asiento.cambiarEstadoAsiento()
            self.reservas.append(reserva) 
            return reserva
        else:
            raise Exception("Asientos ya está ocupado")  
    def venderPasaje(self, pasajero, servicio, asiento, medioPago):
        if(medioPago.validarPago()):
            venta = Venta(pasajero, servicio, asiento, medioPago)
            self.ventas.append(venta)
            return venta
        else:
            raise Exception("El pago ha sido rechazado")


ciudad1 = Ciudad("001","Buenos Aires","Buenos Aires") #Origen
ciudad2 = Ciudad("002","Cordoba","Cordoba") #Destino
ciudad3 = Ciudad("003","Rosario","Santa Fe") #Ciudad de parada
ciudad4 = Ciudad("004","Santa Fe","Santa Fe") #Ciudad de parada

itinerario = Intinerario(ciudad1,ciudad2,[ciudad3,ciudad4])
asientos = [Asiento(i) for i in range(1,6)]
unidad = Unidad("ABC123",asientos)

fecha_partida = datetime(2025,4,20,8,0)
fecha_llegada = datetime(2025,4,20,18,0)

servicio = Servicio(itinerario,unidad,fecha_partida,fecha_llegada,"SemiCama","20000")

argentur = Argentur()
argentur.agregarServicio(servicio)


print("Origen: ",itinerario.verOrigen().verNombre(),". Destino: ",itinerario.verDestino().verNombre(),". Paradas: ")
for j in itinerario.verParadas():
    print(j.verNombre())
