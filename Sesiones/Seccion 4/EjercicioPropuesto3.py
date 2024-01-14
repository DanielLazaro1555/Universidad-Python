"""
Intrucciones de la taeea
En el siguiente ejercicio se solicita calcular el area y el perimetro de un rectangulo, para ello deberemos crear las siguientes variables:

alto (int)
ancho (int)

El usuario debe proporcionar los valores de largo y ancho, y despues se debe imprimir el resultado en el siguiente formato
(No usar acentos y respetar los espacios, mayusculas, minusculas y saltos de lineas):

Proporciona el alto:
Proporciona el ancho:
Area <area>
Perimetro :<perimetro>

Las formulas para calcular el area y el perimtero de un rectangulo son:
Area : alto * ancho
Perimetro : (alto + ancho) * 2
"""
# Resolucion
# Asignamos las variables
alto = int(input("Proporciona el alto del rectangulo : "))
ancho = int(input("Proporciona el ancho del rectangulo : "))
# Asignamos el area
area = alto * ancho
perimetro = ((alto + ancho) * 2)
# Imprimimos el resultado deseado
print("El area es :", area)
print("El perimetro es :", perimetro)
