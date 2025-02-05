# Se solicita incluir la siguiente informacion acerca de un libro:
# titulo
# autor
# Debes imprimir la informacion en el siguiente formato:
# Proporciona el titulo:
# Proporciona el autor:
# <titulo> fue escrito por <autor>

# Resolucion

# Primero pedimos el titulo
titulo = input("Introduce el titulo del libro : ")
# Ahora pedimos el autor
autor = input("Introduce al autor del libro : ")
# Ahora mezclamos todo en una sola frase
print("El libro tiene como titulo",
      titulo, "y fue escrito por", autor)
