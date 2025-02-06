print('*** Operadores de Asignación ***')

# Asignación simple
numero = 5
print(f'Valor de numero: {numero}')
numero = 10
print(f'Valor de numero: {numero}')

cadena = 'Saludos desde Python'
print(f'Valor de cadena: {cadena}')

# Asignación múltiple
x, y, z = 5, 'Hola', -9.15
print(f'Valor de x = {x}, y = {y}, z = {z}')

# Asignación encadenada
a = b = c = 10
print(f'Valor de a = {a}, b = {b}, c = {c}')

# Intercambio de valores de una variable, sin utilizar variables temporales
x, y = 5, 10
print(f'Valores iniciales x = {x}, y = {y}')

# Aplicando el concepto de asignación múltiple, intercambiando valores
x, y = y, x
print(f'Invertir los valores x = {x}, y = {y}')

# Recibir múltiples valores de la entrada del usuario
nombre, apellido = input('Ingrese tu nombre y apellido separados por coma: ').split(',')
print(f'Nombre: {nombre.strip()}, Apellido: {apellido.strip()}')  # Corregido aquí
