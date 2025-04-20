from datetime import datetime
class Airbnb:
    def __init__(self):
        self.hospedajes = []
        self.clientes = []

    def asignarHospedajes(self,hospedaje):
        self.hospedajes.append(hospedaje)
    def asignarCliente(self, cliente):
        self.clientes.append(cliente)
    def mostrarHospedajesCompartidos(self):
        hoy = datetime.today()
        for hospedaje in self.hospedajes:
            for rol in hospedaje.verRoles():
                if(isinstance(rol, Compartido) and rol.tieneBañoPrivado()):
                    for alquiler in hospedaje.alquileres:
                        print("Direccion:",hospedaje.verDireccion(),". Con ",hospedaje.verCapacidad()," habitaciones."," Precio: ",alquiler.verPrecio())

class Alquiler:
    def __init__(self, desde, hasta, precio):
        self.desde = desde
        self.hasta = hasta
        self.precio = precio
    def verPrecio(self):
        pre = self.precio
        return pre

class Hospedaje:
    def __init__(self, capacidad, direccion, anfitrion):
        self.capacidad = capacidad
        self.direccion = direccion
        self.anfitrion = anfitrion
        self.alquileres = []
        self.roles = []
    def agregarRol(self, rol):
        self.alquileres.append(rol)
    def agregarAlquiler(self, alquiler):
        self.alquileres.append(alquiler)
    def verDireccion(self):
        dir = self.direccion
        return dir
    def verCapacidad(self):
        cap = self.capacidad
        return cap
    def verRoles(self):
        rols = self.roles
        return rols
         
class HospedajeRol:
    def __init__(self):
        pass    
        
class Entero(HospedajeRol):
    def __init__(self, ambientes):
        self.ambientes = ambientes

class Privado(HospedajeRol):
    def __init__(self, camas):
        self.camas = camas
        
class Compartido(HospedajeRol):
    def __init__(self, habitaciones, bañoPrivado):
        self.habitaciones = habitaciones
        self.bañoPrivado = bañoPrivado
    def tieneBañoPrivado(self):
        tiene = self.bañoPrivado
        return tiene
        
class Persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        

airbnb = Airbnb()
anfitrion = Persona("Patricio Gnoatto","patricio.gnoatto@gmail.com")
hosp1 = Hospedaje(4,"Guemes 3056",anfitrion)
compartido = Compartido(2,True)
hosp1.agregarRol(compartido)


while True:
    desde_input = input("Ingrese la fecha de inicio del alquiler (formato DD/MM/AAAA)")
    try:
        desde = datetime.strptime(desde_input, "%d/%m/%Y")
        break
    except ValueError:
        print("Formato Incorrecto.Ingrese nuevamente la fecha")
        
while True:
    hasta_input = input("Ingrse la fecha de fin del alquiler (formato DD/MM/AAAA)")
    try:
        hasta = datetime.strptime(hasta_input, "%d/%m/%Y")
        break
    except ValueError:
        print("Formato Incorrecto")    

alquiler1 = Alquiler(desde,hasta,20000)
hosp1.agregarAlquiler(alquiler1)

airbnb.asignarHospedajes(hosp1)

airbnb.mostrarHospedajesCompartidos()

