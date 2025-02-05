# Cadenas en Python

Una **cadena** o **string** en inglés es un tipo de dato que se utiliza para almacenar una **secuencia de caracteres**.

- Las cadenas se deben encerrar entre **comilla doble** (`"`) o **comilla simple** (`'`).
- Los caracteres pueden ser **letras**, **números**, **símbolos** o **espacios**.

## Ejemplo de cadenas en Python

```python
# Cadenas en Python
cadena1 = "Hola Mundo"

📦 Representación en Memoria:

Memoria (Variables): cadena1
Objetos: str ➔ "Hola Mundo"

Este ejemplo muestra cómo se almacena una cadena en la memoria, donde cadena1 hace referencia a un objeto de tipo str que contiene el texto "Hola Mundo".
```

# Detalle de una Cadena

Los **caracteres de una cadena** están **indexados de manera secuencial**.

Por lo tanto, podemos acceder a cada carácter indicando el **índice del carácter** que deseamos recuperar.

## Ejemplo de indexación en Python

```python
cadena1 = "Hola Mundo"

### 📦 Representación en Memoria:

- **Memoria (Variables):** `cadena1`
- **Objetos (String - `str`):**

| **Índice**   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|:------------:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **Carácter** | H | o | l | a |   | M | u | n | d | o |


print(cadena1[0])  # Imprime: H
print(cadena1[4])  # Imprime: (espacio)
print(cadena1[6])  # Imprime: u
```

# Inmutabilidad de una Cadena

Una vez que se crea una **cadena**, los **caracteres dentro de ella no pueden ser modificados**.

Si deseamos modificar una cadena, entonces tenemos que **crear una nueva cadena**.

> ⚠️ **Importante:**  
> Las cadenas **no se pueden modificar**, son **inmutables**.

## Ejemplo de inmutabilidad en Python

```python
cadena1 = "Hola Mundo"
# Intentar modificar directamente un carácter causará un error:
# cadena1[0] = "A"  # ❌ Esto generará un error

# Para modificar una cadena, se debe crear una nueva:
cadena1 = "Adios"
📦 Representación en Memoria:

    Memoria (Variables): cadena1
    Objetos (String - str):
Antes:
cadena1 ---> "Hola Mundo"

Después de la modificación:
cadena1 ---> "Adios"
```

# Caracteres Especiales

Las **cadenas** pueden incluir **caracteres especiales**.

Estos caracteres se introducen usando el **carácter de diagonal invertida** (`\`).  
Ejemplos de caracteres especiales en Python:

- **Nueva Línea:** `\n`  
  Inserta un **salto de línea**.

- **Tabulación:** `\t`  
  Inserta un **tabulador horizontal**, útil para alinear texto.

- **Comilla Simple:** `\'`  
  Permite incluir **comillas simples** en una cadena delimitada por comillas simples.

## Ejemplos en Código Python

```python
# Salto de línea
print("Hola\nMundo")

# Tabulación
print("Nombre:\tDaniel")

# Comilla simple dentro de una cadena
print('Es una cadena con comilla simple: \'Python\'')
```

# Caracteres Especiales (Continuación)

- **Comilla Doble:** `\"`  
  Permite incluir **comillas dobles** en una cadena delimitada por comillas dobles.

- **Barra Invertida:** `\\`  
  Permite incluir una **barra invertida** en la cadena.

> ℹ️ **Nota:**  
> Existen más caracteres especiales, pero estos son los **esenciales**.

## Ejemplos en Código Python

```python
# Comillas dobles dentro de una cadena
print("Esta es una cadena con comillas dobles: \"Python\"")

# Barra invertida dentro de una cadena
print("Esta es una barra invertida: \\")
```

# Concatenación de Cadenas

La **concatenación de cadenas** es una operación que permite **combinar dos o más cadenas** para formar una **nueva cadena**.

En Python existen varias formas de realizar esta operación. Vamos a ver algunas de ellas:

## Uso del operador `+`

El operador `+` es el método más directo para concatenar cadenas.  
Simplemente tenemos que colocar el operador `+` entre las cadenas que deseamos unir.

### Ejemplo

```python
concatenacion = "Hola" + "Mundo"
print(concatenacion)  # Imprime: HolaMundo

concatenacion = "Hola" + " " + "Mundo"
print(concatenacion)  # Imprime: Hola Mundo
```

## Uso de la función `join`

La función `join` nos permite **unir tantas cadenas como necesitemos**.  
Solo necesitamos pasar cada cadena a concatenar, separadas por comas y dentro de una lista.

### Ejemplo

```python
# Uso de la función join para concatenar cadenas
resultado = "".join(["cadena1", "cadena2", "cadena3"])
print(resultado)  # Imprime: cadena1cadena2cadena3

# Concatenación con un separador
resultado = " ".join(["cadena1", "cadena2", "cadena3"])
print(resultado)  # Imprime: cadena1 cadena2 cadena3

```

# Formateo de Cadenas

Python ofrece varias maneras de **formatear cadenas**, que incluyen la capacidad de concatenar texto, variables e incluso aplicar otros tipos de formato, como por ejemplo **indicar el número de decimales** a utilizar en el formato.

## Uso de `f-string` (Python 3.6+)

Esta es la opción **más recomendada**, por ser la **más sencilla**, **rápida** y **legible**.

### Ejemplo de `f-string`

```python
variable = "Mundo"
resultado = f"Hola {variable}"
print(resultado)  # Imprime: Hola Mundo

Ventajas del f-string:

    Es más rápido que otros métodos de formateo.
    Permite insertar expresiones directamente dentro de las llaves {}.
    Es más legible y conciso.

Este método se introdujo en Python 3.6, por lo que se recomienda para proyectos actuales. 🚀
```
