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
