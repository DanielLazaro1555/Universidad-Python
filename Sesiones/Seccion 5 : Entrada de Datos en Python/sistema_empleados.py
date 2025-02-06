print('*** Sistema de Empleados ***')
nombre_empleado = input('Ingrese el nombre del empleado: ')
edad_empleado = int(input('Ingrese la edad del empleado: '))
salario_empleado = float(input('Ingrese el salario del empleado: '))
es_jefe_departamento = input('¿Es jefe de departamento? (Si/No): ')

# Vamos a convertir a un tipo bool la variable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == 'si'

# Imprimir los valores del Empleado
print('\nDatos del Empleado:')
print(f'Nombre: {nombre_empleado}')
print(f'Edad: {edad_empleado}')
print(f'Salario: {salario_empleado:.2f}')
print(f'¿Es jefe de departamento?: {es_jefe_departamento}')
