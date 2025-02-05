# Generador de emails

print('*** Generador de Email ***')

# Nombre completo del usuario
nombre_completo = 'Ubaldo Acosta Soto'
print(f'Nombre usuario: {nombre_completo}')
# Procesar o normalizar el nombre de usuario
# Limpiamos los espacios en blanco al inicio y al final
nombre_usuario = nombre_completo.strip()
# Remplazar los espacios en blanco por puntos
nombre_usuario = nombre_usuario.replace(' ', '.')
# Convertir a minusculas
nombre_usuario = nombre_usuario.lower()
print(f'Nombre de usuario normalizado: {nombre_usuario}')

# Datos de la empresa
nombre_empresa = 'Global Mentoring'
print(f'Nombre empresa: {nombre_empresa}')
extension_dominio = '.com.mx'
print(f'Extension dominio: {extension_dominio}')

# Quitamos los espacios en blanco y convertimos a mayusculas

nombre_empresa_normalizado = nombre_empresa.replace(' ', '').upper()
dominio_email_normalizado = f'@{nombre_empresa_normalizado}{extension_dominio}'
print(f'Dominio email normalizado: {dominio_email_normalizado}')

# Creamos el email final
email = f'{nombre_usuario}{dominio_email_normalizado}'
print(f'\nEmail final generado: {email}')
