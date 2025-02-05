print('***Constantes en Python ***')
PI = 3.1416
print('El valor de PI es:', PI)

NOMBRE_BASE_DATOS = 'clientes_db'
print('El nombre de la base de datos es:', NOMBRE_BASE_DATOS)   # clientes_db

# Esto NO se debe hacer, no se debe modificar el valor de una constante
# TypeError: "NOMBRE_BASE_DATOS" is read-only
NOMBRE_BASE_DATOS = 'listado_clientes_db'
print('No cambiar el valor de una constante:', NOMBRE_BASE_DATOS)

# Usar una constante del lenguaje Python, aunque en este caso no esta en mayusculas
print('Valor de math.pi', math.pi)  # 3.141592653589793