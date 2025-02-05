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

## Uso del método `format`

El método `format` es muy **versátil** y **poderoso**.  
Permite construir **cadenas complejas** de manera flexible.

### Ejemplo de `format`

```python
variable = "Mundo"
resultado = 'Hola {}'.format(variable)
print(resultado)  # Imprime: Hola Mundo

🚀 Ventajas del método format:

    Permite insertar múltiples variables en una sola cadena.
    Se pueden personalizar formatos como números decimales, alineación de texto, etc.
    Útil para construir cadenas más complejas.

Aunque el método format es muy funcional, en versiones recientes de Python se recomienda el uso de f-strings por su simplicidad y rendimiento. 🚀
```

# Métodos de Cadenas

Las **cadenas en Python** vienen con una serie de **métodos útiles** que facilitan su manipulación.  
Por ejemplo:

## 🚀 Métodos Comunes

- **`upper()`** → Cambia las letras a **mayúsculas**.

```python
texto = "hola mundo"
print(texto.upper())  # Imprime: HOLA MUNDO

texto = "HOLA MUNDO"
print(texto.lower())  # Imprime: hola mundo

texto = "   Python   "
print(texto.strip())  # Imprime: Python


```

# Obtener el Largo de una Cadena

Para obtener la **longitud de una cadena**, utilizamos la función incorporada `len()`.

## 🚀 ¿Cómo funciona?

La función `len` funciona con varios tipos de datos, incluyendo:

- **Cadenas de texto**
- **Listas**
- **Tuplas**, entre otros.

Cuando se calcula el largo de una cadena, se toman en cuenta **todos los caracteres**, incluyendo:

- Espacios en blanco
- Caracteres especiales
- Símbolos, etc.

## Ejemplo en Python

```python
cadena1 = 'Hola, Mundo!'
longitud = len(cadena1)

print(longitud)  # Devuelve: 12


📋 Explicación:

    Hola, Mundo! tiene 12 caracteres:
        10 letras + 1 coma + 1 espacio.

La función len() devuelve la cantidad total de caracteres presentes en la cadena. 🚀
```

# Subcadenas en Python

Una **subcadena** es una parte de una cadena principal, y hay varias maneras de **extraer subcadenas en Python**.

Podemos:

- **Extraer subcadenas**
- **Buscarlas**
- **Reemplazarlas**
- Realizar otras operaciones útiles para la manipulación de texto.

## ✂️ Extracción de Cadenas (Slicing)

El **slicing** o **segmentación** permite indicar:

- El **índice de inicio**
- El **índice final** (sin incluir este último carácter)

### 📋 **Sintaxis:**

```python
subcadena = cadena[inicio:fin]

🚀 Ejemplo en Python:

cadena = "Hola, Mundo"
subcadena = cadena[0:4]  # Extrae desde el índice 0 hasta el 3
print(subcadena)         # Imprime: Hola

✅ Explicación:

    inicio es el índice desde donde comienza la subcadena.
    fin es el índice donde termina la subcadena (sin incluir ese carácter).
    En el ejemplo, cadena[0:4] extrae los caracteres en las posiciones 0, 1, 2 y 3.

Este método es muy útil para manipular partes específicas de una cadena en Python. 🚀
```

````
# Subcadenas en Python

## 🔍 Buscar Subcadenas con `find()`

El método `find()` devuelve el **índice de la primera aparición** de la subcadena dentro de una cadena principal.
Si no encuentra la subcadena, devuelve **-1**.

### 📋 **Sintaxis:**

```python
cadena.find(subcadena)

🚀 Ejemplo en Python:

cadena = "Hola mundo"
posicion = cadena.find("mundo")
print(posicion)  # Imprime: 5

cadena = "Hola mundo"
posicion = cadena.find("mundo")
print(posicion)  # Imprime: 5

````

## Subcadenas en Python

## 🔄 Reemplazar Subcadenas con `replace()`

El método `replace()` **reemplaza una subcadena por otra** dentro de una cadena principal.

### 📋 **Sintaxis:**

```python
cadena.replace(subcadena_antigua, subcadena_nueva)


cadena = 'Hola mundo'
nueva_cadena = cadena.replace('mundo', 'a todos')
print(nueva_cadena)  # Imprime: Hola a todos


✅ Explicación:

    La subcadena 'mundo' se reemplaza por 'a todos'.
    El método replace() no modifica la cadena original, sino que devuelve una nueva cadena con el reemplazo realizado.

Este método es muy útil para editar o limpiar textos en Python de manera sencilla. 🚀
```

# Subcadenas en Python

## ✂️ Extraer Subcadenas por Separadores con `split()`

La función `split()` permite **dividir una cadena en una lista de subcadenas** basadas en un **carácter separador**.

### 📋 **Sintaxis:**

```python
cadena.split(separador)

🚀 Ejemplo en Python:

datos = 'Juan,30,México'
lista = datos.split(',')
print(lista)  # Imprime: ['Juan', '30', 'México']
```

✅ Explicación:

    El separador utilizado es la coma (,), lo que permite dividir la cadena en varias partes.
    La función split() devuelve una lista con las subcadenas resultantes.

Este método es muy útil para procesar datos estructurados, como archivos CSV o textos delimitados. 🚀

# 📧 Generador de Email

Crea un programa para **generar un email** a partir de los siguientes datos:

### 📝 **Datos de entrada:**

- **Nombre:** Ubaldo Acosta Soto
- **Empresa:** Global Mentoring
- **Dominio:** com.mx

### 🎯 **Resultado final:**

```python
email = "ubaldo.acosta.soto@globalmentoring.com.mx"

🚀 Código en Python para generar el email:

# Datos de entrada
nombre = "Ubaldo Acosta Soto"
empresa = "Global Mentoring"
dominio = "com.mx"

# Generar el email
email = f"{nombre.lower().replace(' ', '.')}@{empresa.lower().replace(' ', '')}.{dominio}"

# Resultado
print(email)

```

✅ Explicación:

    Se utiliza lower() para convertir todo a minúsculas.
    replace(' ', '.') transforma los espacios del nombre en puntos.
    replace(' ', '') elimina los espacios en el nombre de la empresa.

💡 Salida esperada:
ubaldo.acosta.soto@globalmentoring.com.mx

Este es un ejemplo sencillo para automatizar la creación de correos electrónicos en Python. 🚀

# 📧 Generador de Email

Este es el **resultado del programa** para generar un email a partir de los datos proporcionados.

### 🖨️ **Salida del Programa:**

**_ Generador de Email _** Nombre usuario: Ubaldo Acosta Soto Nombre usuario normalizado: ubaldo.acosta.soto

Nombre empresa: Global Mentoring Extensión del dominio: .com.mx Dominio de email normalizado: @globalmentoring.com.mx

Email final generado: ubaldo.acosta.soto@globalmentoring.com.mx

# 📋 Cuestionario: Cadenas en Python

## 🧪 **Cuestionario 3 | 1 Pregunta**

### ❓ **Pregunta 1:**

¿Cuál opción es correcta para crear la cadena de "Hola Mundo" en Python?

- [ ] `"Hola Mundo'`
- [x] `'Hola Mundo'`
- [ ] `#Hola Mundo#`
- [ ] `'Hola Mundo"`

### ✅ **Respuesta Correcta:** `'Hola Mundo'`

---

## 🎯 **Resultado Final:**

### 🚀 **Explicación:**

En Python, una cadena de texto (o **string**) se puede crear utilizando **comillas simples (`'`) o dobles (`"`)**.  
El ejemplo correcto es `'Hola Mundo'` porque las comillas están bien balanceadas y cerradas correctamente.

---

Este cuestionario es un excelente ejercicio para afianzar conceptos básicos sobre la creación de cadenas en Python. 🚀

![Prueba de la seccion finalizada](Captura%20desde%202025-02-05%2018-49-50.png)
