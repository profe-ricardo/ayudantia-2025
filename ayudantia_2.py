"""
    Crea una función llamada calcular_salario(base, venta1, venta2, venta3) que reciba:
    - el sueldo base de un vendedor,
    - el monto de tres ventas realizadas.
    La comisión es del 10% si el total de ventas supera los $1.000.000.
    La función debe retornar el sueldo total a pagar, incluyendo la comisión si corresponde.
    Ejemplo de uso:
    resultado = calcular_salario(500000, 300000, 400000, 350000)
    print('Sueldo total:', resultado)
"""

def calcular_salario(sueldo, v1, v2, v3):
    total_ventas = v1 + v2 + v3
    comision = 0

    if total_ventas > 1000000:
        comision = total_ventas * 0.1

    return sueldo + comision

# resultado = calcular_salario(500000, 300000, 300000, 500000)
# print('Sueldo total:', resultado)

"""
    Crea una función simular_retiro(saldo_inicial) que simule un cajero automático:
    - Permita hasta 3 intentos para hacer un retiro exitoso.
    - Cada intento debe pedir el monto a retirar.
    - Validar que no sea mayor a 200.000 ni mayor al saldo.
    - Si el retiro es válido, actualizar el saldo y terminar el programa.
    - Si se usan los 3 intentos sin éxito, mostrar 'Tarjeta bloqueada'.
    Ejemplo de uso:
    simular_retiro(150000)
"""

def simular_retiro(saldo_inicial):
    intentos_maximos = False

    for intentos in range(1, 4): # 0, 1, 2, 3, ----
        if saldo_inicial > 0:
            print(f'Intento N°{intentos}')
            monto_retirar = int(input('Ingrese el dinero que quiere retirar: '))

            if monto_retirar > saldo_inicial or monto_retirar > 200000:
                print('Saldo insuficiente')

                if intentos == 3:
                    intentos_maximos = True
                    break
            else:
                print(f'Ha retirado ${monto_retirar}')
                saldo_inicial = saldo_inicial - monto_retirar
                print(f'Nuevo saldo disponible: ${saldo_inicial}')
                break
        else:
            print('Saldo insuficiente')
            break
    
    if intentos_maximos:
        print('Tarjeta bloqueada')

simular_retiro(30000)
    
