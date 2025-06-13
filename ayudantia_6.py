cursos = [
    ['mañana', 30],
    ['tarde', 30],
    ['noche', 15]
]

for i in range(len(cursos)):
    curso = cursos[i][0]
    alumnos = cursos[i][1]
    # print(f"El curso de la {curso} tiene {alumnos} alumnos")

"""
Cada entrada de concierto tiene información fija: (nombre, tipo de entrada, asiento).
    - Crea una tupla con esos datos.
    - Simula mostrar la entrada como un ticket.
    - Justifica por qué no debería permitirse modificar esa entrada después de emitida.
"""

entradas = (
    ('Alex', 'normal', '46A'),
    ('Sebastian', 'premium', '5B'),
    ('Pedro', 'normal', '35F')
)

for i in range(len(entradas)):
    tupla = entradas[i]
    print(f"Cliente {tupla[0]} tiene su entrada en categoría {tupla[1]}, en el asiento {tupla[2]}")