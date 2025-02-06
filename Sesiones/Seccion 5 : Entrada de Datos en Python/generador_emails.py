print('*** Generador de emails ***')

# Solicitar datos del usuario
nombre = input('¿Cuál es tu nombre? ').strip().lower().replace(' ', '.')
apellido = input('¿Cuáles son tus apellidos? ').strip(
).lower().replace(' ', '.')
empresa = input('¿Nombre de tu empresa? ').strip().lower().replace(' ', '.')
extension_dominio = input(
    '¿Extensión del dominio de tu empresa? ').strip().lower().replace(' ', '')

# Generar el email
email = f'{nombre}.{apellido}@{empresa}.{extension_dominio}'

# Mostrar resultado
print(f'\nTu nuevo email generado por el sistema es: {email}\n¡Felicidades!')
