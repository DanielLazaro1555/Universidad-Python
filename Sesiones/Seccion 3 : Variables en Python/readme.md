# 📊 Variables y la Memoria RAM

En **Python**, cada vez que creamos una variable y le asignamos un valor, estamos reservando espacio en la memoria **RAM** (_Random Access Memory_), también conocida como memoria de corto plazo.

---

## 🚀 Ejemplo Práctico

```python
edad = 30
altura = 1.75

edad = 32


🧠 Explicación Detallada

    Asignación Inicial de Variables:
        edad = 30 → Se crea un objeto int con el valor 30 en la memoria RAM.
        altura = 1.75 → Se crea un objeto float con el valor 1.75 en la memoria RAM.

    Reasignación de Variable:
        edad = 32 → La referencia al valor anterior (30) se elimina.
        La variable edad ahora apunta a un nuevo objeto int con el valor 32.

    ⚡ Nota: En Python, cuando se reasigna un valor a una variable, el objeto anterior en memoria puede quedar sin referencia y ser eliminado por el recolector de basura.
```

## 🗂️ Representación en Memoria

| **Variable** | **Valor** | **Tipo de Dato** | **Dirección de Memoria** |
| :----------: | :-------: | :--------------: | :----------------------: |
|    `edad`    |   `32`    |      `int`       |         `0x555`          |
| _(liberado)_ |   `30`    |      `int`       |         `0x333`          |  
|   `altura`   |  `1.75`   |     `float`      |         `0x444`          |
