"""
    Crea una función login(usuario,	clave) que verifique
    si los datos coinciden con los valores 'admin' y '1234'.
    Debe retornar True si los datos	son	correctos,
    y False	si no lo son.
"""

def login(usuario, clave):
    if (usuario == 'admin' and clave == '1234'):
        return True
    else:
        return False

# user = str(input("Ingrese su usuario: "))
# password = str(input("Ingrese su clave: "))
# validacion = login(user, password)
# print(validacion)
    
"""
    Crea una función interpretar_temperatura(temp) que reciba una temperatura
    como número entero y retorne un mensaje según el rango:
    - menor a 0 -> 'Temperatura muy baja'
    - entre 0 y 20 -> 'Temperatura normal'
    - mayor a 20 -> 'Temperatura elevada'
"""

def interpretar_temperatura(temp):
    if (temp < 0):
        return 'Temperatura muy baja'
    elif (temp >= 0 and temp <= 20):
        return 'Temperatura normal'
    else:
        return 'Temperatura elevada'
    
temp = int(input("Ingrese la temperatura: "))
validacion = interpretar_temperatura(temp)
print(validacion)