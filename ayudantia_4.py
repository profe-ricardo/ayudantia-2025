"""
    Ejercicio 1: Control de producción de etiquetas en turnos (30 puntos)

    Una empresa imprime etiquetas para productos.
    Cada trabajador debe imprimir una cantidad durante su turno.
    Crea una función llamada control_etiquetas(nombre, turno, meta_turno) que:
        1. Pida al usuario cuántas etiquetas ha impreso hasta ahora (usando un ciclo while acumulativo).
        2. El turno termina cuando el usuario digita 0 como cantidad (esto indica que finalizó el turno).
        3. Al final, debe mostrar: - "Operario [nombre] en turno [turno] imprimió un total de [total] etiquetas." - Si alcanzó la meta: "¡Meta cumplida!" - Si no la alcanzó: "Meta no alcanzada. Faltaron [X] etiquetas."
"""

def control_etiquetas(nombre, turno, meta_turno):
    etiquetas_ingresadas = 1
    etiquetas_totales = 0

    while etiquetas_ingresadas != 0:
        etiquetas = int(input("Etiquetas ingresadas hasta el momento: "))
        etiquetas_ingresadas = etiquetas
        etiquetas_totales += etiquetas

    print(f"Operario {nombre} en turno {turno} imprimió un total de {etiquetas_totales} etiquetas.")

    if (etiquetas_totales < meta_turno):
        etiquetas_faltantes = meta_turno - etiquetas_totales
        print(f"Meta no alcanzada. Faltaron {etiquetas_faltantes} etiquetas.")
    else:
        print("¡Meta cumplida!")
        
# nombre_trabajador = str(input("Ingrese su nombre: "))
# turno_trabajador = str(input("Ingrese su turno: "))
# meta = int(input("Ingrese la meta del turno: "))

# control_etiquetas(nombre_trabajador, turno_trabajador, meta)

"""
    Ejercicio 2: Registro de pasos correctos en línea de ensamblaje (40 puntos)

    En una línea de ensamblaje, un operario revisa una serie de pasos que deben ser exitosos.
    Crea una función registro_ensamblaje(total_pasos) que:
        1. Pida al usuario ingresar el resultado de cada paso (1 si fue exitoso, 0 si falló).
        2. Valide que solo se pueda ingresar 1 o 0. Si se escribe otro valor, debe pedir nuevamente el mismo paso.
        3. Al finalizar, la función debe mostrar:
            - La cantidad total de pasos exitosos y fallidos.
            - El porcentaje de éxito.
            - Y un mensaje según el resultado:
                • 90% o más: "Producción óptima"
                • Entre 70% y 89%: "Producción aceptable"
                • Menos de 70%: "Producción deficiente"
"""

def registro_ensamblaje(total_pasos):
    acumulador = 0

    for i in range(total_pasos):
        while True:
            resultado = int(input("Ingrese el resultado del paso (1 o 0): "))

            if resultado == 1 or resultado == 0:
                break
            else:
                print("Debe ingresar 1 o 0")
        
        if resultado == 1:
            acumulador += 1

    pasos_fallidos = total_pasos - acumulador
    porcentaje = acumulador * 100 / total_pasos
        
    print("Finaliza ejecución")
    print(f"{acumulador} pasos exitosos")
    print(f"{pasos_fallidos} pasos fallidos")
    print(f"Hubo un {porcentaje}% de éxito")

    if porcentaje >= 90:
        print("Producción óptima")
    elif porcentaje >= 70:
        print("Producción aceptable")
    else:
        print("Producción deficiente")
    
pasos = int(input("Ingrese la cantidad total de pasos: "))
registro_ensamblaje(pasos)