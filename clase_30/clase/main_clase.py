class Persona:
    def __init__(self,dni,nac,fecha_nac):
        self.dni = dni
        self.nac = nac
        self.fecha_nac = fecha_nac

    def es_usuario(self):
        pass




class Premium(Persona):
    status = "premium"

    def __init__(self,ttl):
        self.ttl = ttl

    def premium(self):
        print(f"{self.nombre}-soy un usuario premium")

    def es_usuario(self):
        print(f"soy un usuario premmium hasta {self.ttl}")



class Validador:
    def checkear(self, status):
        if status :
            print("es cliente actual")
        else:
            print("no es cliente, no me interesa serlo")

class PosibleCliente:
    status = False

    def es_usuario(self):
        if self.status:
            print(f"soy cliente")
        else: 
            print("no lo soy!")
    def clientela(self,validador:Validador):
        validador.checkear(self.status)


class Cliente(Premium):
    def __init__(self, nombre,ttl):
        Premium.__init__(self, ttl)
        self.nombre = nombre

    def premium(self):
        print(f"{self.nombre}-soy un usuario premium por {self.ttl}")

    def es_usuario(self):
        print(f"soy un cliente, por eso soy premium igual")

    
class Usuario(Premium):

    def __init__(self,nombre,cbu,passwd):
        self.nombre =  nombre
        self.__cbu = cbu
        self.passwd = passwd

    def get_cbu(self):
        return self.__cbu

cliente1 = Usuario(
    "javier",
    1892739123131987123,
    "soy un passwd secreto"
    )

print(cliente1.get_cbu())

cliente1.__cbu = 98908098908
print(cliente1.__cbu)
print(cliente1.get_cbu())


cliente1.premium()
print(cliente1.status)



miguel = Cliente("miguel","1 mes")
miguel.premium()
miguel.es_usuario()


manuela = PosibleCliente()
manuela.es_usuario()

obj_validador = Validador()
manuela.clientela( obj_validador )

