# Conversion de tipos de datos

# Conversion de cadena a numero

numero_cadena = '10'
numero_entero = int(numero_cadena)
print(f'Valor numerico en cadena: {numero_entero}')
print(f'Cadena a entero: {numero_entero}')

# Converti de cadena a flotante
numero_cadena = '3.14'
numero_flotante = float(numero_cadena)
print(f'Cadena a flotante: {numero_flotante}')

# Convertir de numero a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f'Numero a cadena: {numero_cadena}')

# Convertir a booleano


# Tipo bool es False en los siguientes casos
# Si el valor es 0, cadena vacia, o None, entonces regresa False
# Regresa verdadero, si el valor es distinto de 0, cadena no vacia,si es distinto de cadena vacia
# y tambien si es distinto a None
numero_entero = 0
booleano = bool(numero_entero)
print(f'Valor booleano de 0: {booleano}')  # False

numero_entero = 5
print(f'Valor booleano de 0: {booleano}')  # True

cadena = ''
booleano = bool(cadena)
# Falso, incluye colecciones vacias
print(f'Valor booleano de cadena vacia: {booleano}')

cadena = 'Cadena con valor'
booleano = bool(cadena)
print(f'Valor booleano de cadena No vacia: {booleano}')  # Verdadero

variable = None
booleano = bool(variable)
print(f'Valor booleano de None: {booleano}')  # False
