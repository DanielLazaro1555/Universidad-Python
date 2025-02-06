# Operadores en Python

Los **operadores** son símbolos especiales que están diseñados para realizar **operaciones específicas**. Tenemos varios tipos, como son:

## Operadores Aritméticos

Permiten realizar **cálculos matemáticos básicos**, como **suma, resta, multiplicación o división**.

## Operadores de Asignación

Se utilizan para **asignar valores** a variables.

## Operadores de Comparación

Se utilizan para **comparar un valor con otro**.

## Operadores Lógicos

Se utilizan para **combinar expresiones condicionales o lógicas**.

## Operadores de Identidad

Se utilizan para **comparar si dos variables son el mismo objeto**.

## Operadores de Membresía

Se utilizan para **probar si una secuencia** (Ej. una subcadena) **se presenta en un objeto**.

# Operadores Aritméticos

Los operadores aritméticos nos permiten realizar cálculos matemáticos básicos entre números.  
Por ejemplo:

- **Suma (`+`)**: Suma dos operandos.
- **Resta (`-`)**: Resta dos operandos.
- **Multiplicación (`*`)**: Multiplica dos operandos.
- **División (`/`)**: Divide el primer operando entre el segundo.  
  _Resultado:_ Un valor flotante.
- **División Entera (`//`)**: Divide el primer operando entre el segundo.  
  _Resultado:_ Un número entero.
- **Módulo (`%`)**: Regresa el residuo de la división.
- **Exponente (`**`)\*\*: Eleva el primer operando a la potencia del segundo.

# Operadores de Asignación en Python

El operador de asignación se utiliza para asignar un valor a una variable, y se usa el caracter (`=`).

## Sintaxis del operador de asignación

```python
# Sintaxis operador asignación
variable = valor

Ejemplo de operador de asignación

# Ejemplo de Operador Asignación
numero = 10
texto = "Hola, mundo"

Asignación Múltiple en Python

Sintaxis de asignación múltiple
# Sintaxis de Asignación Múltiple
variable1, variable2 = valor1, valor2

Ejemplo de asignación múltiple
# Ejemplo de Asignación Múltiple
a, b, c = 10, "Saludos", 14.5
```

Asignación Encadenada

En Python también contamos con la asignación encadenada. Esto permite asignar el mismo valor a múltiples variables.

Sintaxis de asignación encadenada

# Sintaxis de Asignación Encadenada

variable1 = variable2 = ... = valor

Ejemplo de inicialización de contadores

# Ejemplo. Inicializar contadores

contador1 = contador2 = 0

Operadores de Asignación Compuestos

Los operadores de asignación compuestos combinan una operación aritmética con una asignación, haciendo las operaciones más concisas.

Los operadores pueden ser: +=, -=, \*=, /=, etc.
Sintaxis de operador de asignación compuesto

# Sintaxis Operador Asignación Compuesto

variable OPERADOR= valor

Ejemplo de operador de asignación compuesto

# Ejemplo Operador Asignación Compuesto

contador = 0
contador += 1 # contador = contador + 1

# Operadores de Comparación

Los operadores condicionales se utilizan para comparar dos valores.

El resultado siempre es un valor booleano `True` o `False`, dependiendo de si la condición se cumple o no.

## Operador de Igualdad (`==`)

Compara si dos valores son iguales.

### Sintaxis del operador de igualdad

```python
# Sintaxis operador igualdad
a == b

Ejemplo del operador de igualdad

# Ejemplo operador igualdad
print(5 == 5)  # True
print(5 == 6)  # False

Operador Distinto (!=)

Compara si dos valores son distintos.
Sintaxis del operador distinto

# Sintaxis operador distinto
a != b

Ejemplo del operador distinto

# Ejemplo operador distinto
print(5 != 5)  # False
print(5 != 6)  # True
```

# Operadores de Comparación

Los operadores condicionales se utilizan para comparar dos valores.

El resultado siempre es un valor booleano `True` o `False`, dependiendo de si la condición se cumple o no.

## Operador menor que (`<`)

Compara si el valor de la izquierda es menor que el de la derecha. Si es menor devuelve `True`, sino `False`.

```python
# Ejemplo operador menor que
print(3 < 5)  # True
print(5 < 3)  # False

Operador menor o igual que (<=)

Verifica si el valor de la izquierda es menor o igual al de la derecha. Si es menor o igual devuelve True, sino False.

# Ejemplo operador menor o igual que
print(3 <= 5)  # True
print(5 <= 5)  # True
print(6 <= 5)  # False

Operador mayor que (>)

Si el valor de la izquierda es mayor que el de la derecha, regresa True, sino False.

# Ejemplo operador mayor que
print(5 > 3)  # True
print(3 > 5)  # False

Operador mayor o igual que (>=)

Si el valor de la izquierda es mayor o igual que el de la derecha, regresa True, sino False.

# Ejemplo operador mayor o igual que
print(5 >= 3)  # True
print(5 >= 5)  # True
print(3 >= 5)  # False
```
