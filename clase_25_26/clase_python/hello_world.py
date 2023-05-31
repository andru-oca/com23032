# MI PRIMER ARCHIVO DE PYTHON

"""
SEGUNDO COMENTARIO 
PERO EN BLOQUE
"""

# texto_saludo = "hola mundo"

# texto_saludo_hints:int = "hola mundo"  # no afecta en el programa los hints

# print(texto_saludo , '\n', texto_saludo_hints)


# ------------------------

# edad = input("ingrese la edad :\n")
# edad = int(edad)

# edad += 1 # => edad = edad + 1

# print("edad es: \t", edad)

# -----------------------------

# condicionales

# if edad > 50 :
#     print("sos mayor que 50")
# elif edad >=18 : 
#     print("sos mayor que 18")
# else: 
#     print("sos menor")


# -----------------------------

# iteradores  FOR - WHILE 


texto_normal = """
    Esta afirmación, cuya autoría es de Osho,
    traduce al lenguaje de las frases positivas y motivadoras la filosofía de los filósofos existencialistas.
    Podemos hacer que todo lo que hacemos esté conectado con algo significativo para nosotros.
"""

# for char in texto_normal:
#     if char == "l":
#         print("apareció una L!!")

for numero in range(20,40,4):
    print(numero)


# while



# edad = input("ingrese la edad :\n")
# edad = int(edad)

# while edad < 18:
#     print("sos menor no podes pasar, intenta de nuevo")
#     edad = input("ingrese la edad :\n")
#     edad = int(edad)
# else:
#     print("ahora si tenes mas de 18 años")

# flag = True

# while flag:
#     edad = input("ingrese la edad :\n")
#     edad = int(edad)
    
#     if edad > 18:
#         print("es mayor a 18")
#         flag = False

#     print("no es mayor, intentá de nuevo")

# else:
#     print("sale por aca?")


from functions_custom.funciones import UUID

print(UUID)




