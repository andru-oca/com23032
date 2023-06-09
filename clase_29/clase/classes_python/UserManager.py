from .Usuario import Usuario

class UserManager:
    db_user = []

    def __init__(self,**kwargs):
        self.path:str = kwargs["path"]
        self.nombre:str = kwargs["nombre"]
        self.encargado_nombre:str = kwargs["encargado_nombre"]


    def create_usuario_beer(self, usuario:Usuario):
        self.db_user.append(usuario)
        print(f"El usuario : {usuario.nombre} ha sido agregado")


    def read_usuarios_beer(self):
        for usuario in self.db_user:
            print(usuario.esta_activo())

    def update_usuario(self,nombre_usuario,preferencia):
        for index,usuario in enumerate(self.db_user):
            if usuario.nombre == nombre_usuario:
                usuario.preferencias = preferencia       


    def delete_usuario(self, nombre):
        # self.db_user = [
        #    user for user in self.db_user if user.nombre != nombre
        # ]

        for index,usuario in enumerate(self.db_user):
            if usuario.nombre == nombre:
                self.db_user.pop(index)




