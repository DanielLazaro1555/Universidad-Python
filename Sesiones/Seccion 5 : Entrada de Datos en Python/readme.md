# 🔄 Conversión de Tipos de Datos en Python

La **conversión de tipos de datos**, también conocida como **casting**, es una técnica utilizada para **manipular datos** que no están en el tipo requerido.

---

## 🔹 ¿Para qué sirve?

A veces, los datos ingresados o procesados no tienen el tipo adecuado y necesitamos convertirlos para que sean compatibles con nuestras operaciones.

Podemos hacer **conversiones entre distintos tipos de datos** en Python.

---

## 🚀 **Funciones de Conversión en Python**

| **Conversión**           | **Función en Python** |
| ------------------------ | --------------------- |
| Convertir a **entero**   | `int()`               |
| Convertir a **flotante** | `float()`             |
| Convertir a **cadena**   | `str()`               |
| Convertir a **booleano** | `bool()`              |

---

## 📝 **Ejemplo de Conversión en Python**

```python
# Convertir a entero
numero_entero = int(3.8)
print(numero_entero)  # Imprime: 3

# Convertir a flotante
numero_flotante = float(5)
print(numero_flotante)  # Imprime: 5.0

# Convertir a cadena
cadena = str(100)
print(cadena)  # Imprime: '100'

# Convertir a booleano
valor_booleano = bool(0)
print(valor_booleano)  # Imprime: False
```

# ⌨️ Entrada de Datos por Consola en Python

En **Python**, la entrada de datos se realiza usando la función `input()`.

---

## 🔹 ¿Cómo funciona?

- La función `input()` **pausa la ejecución del programa** y espera a que el usuario introduzca algún texto desde el teclado.
- Una vez que el usuario presiona **Enter**, el texto introducido se **devuelve como una cadena (`str`)**.

---

## 🚀 **Ejemplo de uso en Python:**

```python
# Solicitar entrada de datos al usuario
nombre = input("Ingrese su nombre: ")

# Mostrar la entrada recibida
print("Hola,", nombre)
```

✅ Explicación:

    El programa muestra el mensaje "Ingrese su nombre: " y espera una respuesta del usuario.
    Cuando el usuario escribe algo y presiona Enter, el valor ingresado se guarda en la variable nombre.
    Luego, se imprime un mensaje personalizado con el nombre ingresado.

🔥 Importante:

    input() siempre devuelve una cadena de texto (str), aunque se ingresen números.
    Si se necesita un número, hay que convertir el valor con int() o float(), por ejemplo:

edad = int(input("Ingrese su edad: "))
print("Tienes", edad, "años.")

Si el usuario ingresa "25", Python lo convierte a un entero (int) para que pueda ser usado en cálculos.

📌 La función input() es fundamental para hacer programas interactivos en Python. 🚀

# 🏢 Sistema de Empleados

Crea un programa para **solicitar la información de un empleado**, introduciendo los datos **por consola**.

---

## 📋 **Datos a Solicitar:**

- **Nombre del Empleado**
- **Edad del Empleado** _(convertir a entero `int`)_
- **Salario del Empleado** _(convertir a flotante `float`)_
- **Es jefe de departamento** _(responder con "Sí" o "No")_

---

## 🚀 **Código en Python para Solicitar los Datos**

```python
# Solicitar datos al usuario
nombre = input("Ingrese el nombre del empleado: ")
edad = int(input("Ingrese la edad del empleado: "))
salario = float(input("Ingrese el salario del empleado: "))
es_jefe = input("¿Es jefe de departamento? (Si/No): ").strip().lower() == "si"

# Mostrar los datos ingresados
print("\n--- Información del Empleado ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Salario: ${salario:.2f}")
print(f"Jefe de Departamento: {'Sí' if es_jefe else 'No'}")
```

✅ Explicación del Código:

    Se solicita cada dato con input().
    Conversión de tipos de datos:
        int(input()) para la edad (ya que debe ser un número entero).
        float(input()) para el salario (para admitir decimales).
    Para el campo "¿Es jefe de departamento?", se usa .strip().lower() == "si" para convertir la respuesta a True o False.
    Se imprime la información del empleado con formato claro.

📌 Ejemplo de Entrada y Salida:

Entrada del usuario:
Ingrese el nombre del empleado: Juan Pérez
Ingrese la edad del empleado: 35
Ingrese el salario del empleado: 1500.75
¿Es jefe de departamento? (Si/No): si

Salida esperada en la consola:
--- Información del Empleado ---
Nombre: Juan Pérez
Edad: 35 años
Salario: $1500.75
Jefe de Departamento: Sí

🚀 Este programa permite capturar datos de empleados de manera interactiva en Python.

# 🍽️ Receta de Cocina

Crea un programa para solicitar **valores importantes** de una **receta de cocina** y luego imprimir los datos ingresados.

---

## 📋 **Valores que debe introducir el usuario:**

- **Nombre de la Receta**
- **Ingredientes** _(separados por comas)_
- **Tiempo de preparación** _(en minutos - convertir a `int`)_
- **Dificultad** _(Opciones: "Fácil", "Media", "Alta")_

---

## 🚀 **Código en Python para Solicitar los Datos**

```python
# Solicitar datos al usuario
nombre_receta = input("Ingrese el nombre de la receta: ")
ingredientes = input("Ingrese los ingredientes (separados por comas): ").split(",")
tiempo_preparacion = int(input("Ingrese el tiempo de preparación (en minutos): "))
dificultad = input("Seleccione la dificultad (Fácil, Media, Alta): ").capitalize()

# Mostrar la receta ingresada
print("\n--- Receta de Cocina ---")
print(f"📌 Nombre: {nombre_receta}")
print(f"🥄 Ingredientes: {', '.join(ingredientes)}")
print(f"⏳ Tiempo de Preparación: {tiempo_preparacion} minutos")
print(f"🔥 Dificultad: {dificultad}")

✅ Explicación del Código:

    Se solicitan los datos al usuario con input().
    Conversión de datos:
        split(",") separa los ingredientes por comas y los almacena en una lista.
        int(input()) convierte el tiempo de preparación a un número entero.
        .capitalize() asegura que la dificultad inicie con mayúscula (Ej: "Media" en vez de "media").
    Se imprime la receta con formato claro.

📌 Ejemplo de Entrada y Salida:

Entrada del usuario:

Ingrese el nombre de la receta: Ensalada César
Ingrese los ingredientes (separados por comas): Lechuga, Pollo, Queso, Pan, Salsa César
Ingrese el tiempo de preparación (en minutos): 15
Seleccione la dificultad (Fácil, Media, Alta): facil

Salida esperada en la consola:

--- Receta de Cocina ---
📌 Nombre: Ensalada César
🥄 Ingredientes: Lechuga, Pollo, Queso, Pan, Salsa César
⏳ Tiempo de Preparación: 15 minutos
🔥 Dificultad: Fácil
```

# 🎲 Generar Valores Aleatorios en Python

En **Python**, podemos generar **números aleatorios** utilizando la función `randint()` del módulo `random`.

---

## 🔹 **¿Cómo funciona `randint()`?**

La función `randint(a, b)` genera un **número entero aleatorio** entre `a` y `b`, **incluyendo ambos valores**.

```python
import random

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime un número entre 1 y 10 (incluidos)

```

📌 Importar el Módulo random

Antes de usar la función randint(), es necesario importar el módulo random.
📜 Sintaxis para importar un módulo en Python:

import random
🚀 Ejemplo Completo en Python

import random

# Generar un número aleatorio entre 5 y 20

numero = random.randint(5, 20)

print(f"El número aleatorio generado es: {numero}")

📌 Salida esperada:

El número aleatorio generado es: 12 # (puede variar en cada ejecución)

🎯 Conclusión

randint(a, b) devuelve un número aleatorio entre a y b, incluyendo ambos extremos.
Es necesario importar el módulo random antes de usar la función.
Python ofrece muchas más funciones en random, como random.random() para valores decimales entre 0 y 1.

🚀 Generar números aleatorios es clave para juegos, simulaciones y pruebas en Python. 🎲🔥

# 🆔 Sistema Generador de ID Único

Se solicita crear un sistema para **generar un ID único** para cada persona.

---

## 📋 **El sistema debe solicitar al usuario:**

- **Nombre**
- **Apellido**
- **Año de Nacimiento** _(Formato: `YYYY`)_

---

## 🚀 **Código en Python para Generar un ID Único**

```python
import random

# Solicitar datos al usuario
nombre = input("Ingrese su nombre: ").strip().lower()
apellido = input("Ingrese su apellido: ").strip().lower()
anio_nacimiento = input("Ingrese su año de nacimiento (YYYY): ").strip()

# Generar un número aleatorio para hacerlo único
numero_unico = random.randint(100, 999)

# Crear el ID único combinando los datos
id_unico = f"{nombre[:3]}{apellido[:3]}{anio_nacimiento[-2:]}{numero_unico}"

# Mostrar el ID generado
print("\n--- ID Generado ---")
print(f"🆔 Su ID único es: {id_unico}")

```

## 🔢 Reglas para la Generación del ID Único

El sistema debe realizar los siguientes pasos con los datos ingresados por el usuario:

1. **Del valor recibido del nombre:**

   - Usar solo las **2 primeras letras** y convertirlas a **mayúsculas**.

2. **Del valor del apellido:**

   - Usar las **2 primeras letras** y convertirlas a **mayúsculas**.

3. **Del valor del año de nacimiento:**

   - Tomar **los últimos 2 dígitos**.

4. **Generar un número aleatorio de 4 dígitos** con `randint()`.

5. **Unir todos los valores** en un solo string para obtener el ID único.

---

## 📌 **Ejemplo de Conversión de Datos**

| Dato Original                     | Transformación |
| --------------------------------- | -------------- |
| **Nombre:** Juan                  | `JU`           |
| **Apellido:** Pérez               | `PE`           |
| **Año de Nacimiento:** 1995       | `95`           |
| **Número Aleatorio:** `randint()` | `7326`         |

**🔹 Resultado Final:**

# 📧 Sistema Generador de Emails

Se solicita crear una nueva versión del sistema generador de emails.

## 📌 Para generar un email se debe solicitar:

- **Nombre** → Ej. _Juan Carlos_
- **Apellidos** → Ej. _Gómez Lara_
- **Nombre Empresa** → Ej. _Global Mentoring_
- **Extensión Dominio** → Ej. _.com.mx_

---

## 📩 **El resultado debe ser**:

juan.carlos.gomez.lara@globalmentoring.com.mx
