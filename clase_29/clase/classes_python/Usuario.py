class Usuario:
    """
    ATRIBUTOS DE CLASE
    """
    activo = True

    """
    ATRIBUTOS DE INSTANCIA
    """
    # def __init__(self, nombre, dni, preferencias):
    #     self.nombre = nombre
    #     self.dni = dni
    #     self.preferencias = preferencias

    def __init__(self,**kwargs):

        self.nombre:str = kwargs['nombre']
        self.dni:int = kwargs['dni']
        self.preferencias:list = kwargs['preferencias']
        self.puntos:int = kwargs.get("puntos",0)
        

    def __str__(self):
        return f"""
            Soy {self.nombre}
            -----
            {self.esta_activo()}
        
        """
        

    def esta_activo(self):
        if self.activo:
            return f"{self.nombre}\nEstoy disponible para comprar"
        else:
            return f"{self.nombre}\nNO puedo comprar"

    def add_preferencia(self, nombre_preferencia):
        self.preferencias.append(nombre_preferencia)