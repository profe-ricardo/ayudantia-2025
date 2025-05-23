"""
    Desarrolle un pseudocódigo para un sistema de monitoreo que revisa la temperatura 
    de 16 máquinas. Si una máquina supera los 90 °C, se debe activar una alerta de 
    sobrecalentamiento. En caso contrario hay que indicar que la máquina está
    funcionando normalmente. Al final de revisar todas las máquinas indicar cuántas de 
    éstas tuvieron sobrecalentamiento y un promedio de todas las temperaturas de las 
    16 máquinas.
"""

def main():
    temperaturas = []

    for i in range(0, 5):
        contador = i + 1
        ingreso = float(input(f"Ingrese la temperatura de la máquina {contador}: "))
        temperaturas.append(ingreso)

    promedio = 0
    maquinas_sobrecalentadas = 0

    for j in range(len(temperaturas)):
        contador = j + 1

        if temperaturas[j] > 90:
            print(f"La máquina {contador} está con sobrecalentamiento")
            maquinas_sobrecalentadas += 1
        else:
            print(f"Máquina {contador} con temperatura normal")

        promedio += temperaturas[j]
    
    promedio = promedio / len(temperaturas)
    print(f"Hubo {maquinas_sobrecalentadas} maquinas sobrecalentadas")
    print(f"El promedio de temperatura fue: {promedio}")

main()