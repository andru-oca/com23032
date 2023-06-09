
# NECESITO GENERAR UN PROYECTO QUE ME PERMITA DAR DE ALTA BAJA LECTURA Y MODIFICACION DE USUARIOS 
# QUE COMPRAR UNA CERVEZA

from classes_python.Usuario import Usuario
from classes_python.UserManager import UserManager


# mariano es un objeto
mariano = Usuario(
    nombre      = "mariano",
    dni         = 9891723,
    preferencias= ['js','py','rust'],
    puntos      = 100
)

pers    = Usuario(
    nombre      = "pers",
    dni         = 9891787,
    preferencias= ['java','golang']
)

beta_tester = Usuario(
    nombre      = "test",
    dni         = 0000,
    preferencias= [],
    puntos      = 1000
)


mariano.activo = False

# print(pers)


beer_manager = UserManager(
    path = "/sarasa/path/etc",
    nombre = "cerveceria" ,
    encargado_nombre = "Miguel"
)


print(beer_manager.db_user)

print("INSERT DATABASE")
beer_manager.create_usuario_beer(pers)
beer_manager.create_usuario_beer(mariano)
beer_manager.create_usuario_beer(
    Usuario(
        nombre      = "Sofia",
        dni         = 46123,
        preferencias= ['js','ruby'],

    )
)
print("-"*50)
print(beer_manager.db_user)
print("READ DATABASE")
beer_manager.read_usuarios_beer()

print("DELETE USER FROM DATABASE")
beer_manager.delete_usuario("mariano")
beer_manager.read_usuarios_beer()


print("UPDATE USER FROM DATABASE")
beer_manager.update_usuario("pers",['COBOL'])

for user in beer_manager.db_user:
    if user.nombre == "Sofia":
        user.add_preferencia("Carbon")
    print(f"{user.nombre} ==> {user.preferencias}")