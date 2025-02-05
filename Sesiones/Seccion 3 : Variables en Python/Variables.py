# Ejemplos de uso de variables en Python

# Llamando desde las variables
mivariable = "Hola desde Python"
print(mivariable)

# Cambiando el valor de la variable
mivariable = 2  # Ahora es un número entero
print(mivariable)

# Cambiando a otro valor numérico
mivariable = 10  # Valor entero
print(mivariable)

#####################################################

# Sintaxis para definir una variable
nombre_de_la_variable = "valor de la variable"

# Declaración de variables y asignación de valores
nombre = "Maria"       # Cadena de texto (str)
edad = 30              # Número entero (int)
peso = 65.5            # Número decimal o de punto flotante (float)
es_casado = False      # Valor booleano (bool)

# Mostrando las variables en consola
print("Nombre:", nombre)
print("Edad:", edad)
print("Peso:", peso)
print("¿Está casado?:", es_casado)

#######################################################

# Variables en python

# Declaración e inicialización de variables

edad = 28  # Valor tipo Entero
altura = 1.65  # Valor tipo Flotante
pais = 'Mexico'  # Valor tipo Cadena

# Acceder a las variables
print('Edad:', edad)
print('Altura:', altura)
print('País:', pais)

# Modificar el valor de una variable
edad = 30
altura = 1.68

# Acceder a las variables
print('Valores modificados:')
print('Edad:', edad)
print('Altura:', altura)
print('País:', pais)

# En python el tipo es dinámico

edad = 'Treinta'
print('Edad:', edad)

# Si queremos acceder a una variable no declarada manda error
telefono = '123456789'
print('telefono:', telefono)

# Regla y convenciones en nombres de variables

# Ejemplos de reglas estrictas
nombre_usuario = 'Juan Perez'  # Correcto
# 1nombre_usuario = 'Karla Gomez'  # Incorrecto

# No podemos usar palabras reservadas
# class = 'Mi clase'  # Incorrecto
klass = 'Mi clase'

# Sensibles a mayúsculas y minúsculas
nombre = 'Juan'
nombre = 'Karla'
print(nombre)
print(nombre)
# print(NOMBRE) esta variable no ha sido definida

# Snake case
nombre_completo = 'Ricardo Esparza'
print(nombre_completo)

# Prefijos y sufijos
es_casado = False
nombre_txt = 'archivo.txt'
