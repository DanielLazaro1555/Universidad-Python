import random  # Importar el módulo random

print('*** Sistema de generación de ID único ***')

# Solicitar datos al usuario
nombre = input('¿Cuál es tu nombre? ').strip()
apellido = input('¿Ingrese su apellido? ').strip()
# YYYY - Formato correcto
año_nacimiento = input('¿Cuál es tu año de nacimiento? (YYYY) ').strip()

# Normalizar los valores
# Tomar las 2 primeras letras del nombre en mayúsculas
nombre_2 = nombre.upper()[:2]
# Tomar las 2 primeras letras del apellido en mayúsculas
apellido_2 = apellido.upper()[:2]
# Tomar los últimos 2 dígitos del año de nacimiento
año_nacimiento_2 = año_nacimiento[-2:]

# Generar el valor aleatorio
aleatorio = random.randint(1000, 9999)  # Número aleatorio de 4 dígitos

# Generamos el valor de ID único
id_unico = f'{nombre_2}{apellido_2}{año_nacimiento_2}{aleatorio}'

# Mensaje final con correcciones en los espacios y formato
print(f'\nHola {
      nombre}, tu número de identificación (ID) generado por el sistema es: {id_unico}')
print('¡Felicidades!')
