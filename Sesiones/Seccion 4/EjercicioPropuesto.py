# Ejercicio - Califica tu dia del 1 al 10

# Primero asignamos las variables
numerolimite = int(input("Califica tu dia del 1 al 10 : "))

# Creamos una condicional

if numerolimite < 10:
    print("Tuviste un excelente dia con calificacion de " + str(numerolimite))
else:
    print("Te pasaste")



#Manera resuelta por el Docente
resultado = input('Como estuvo tu dia (1 al 10)? : ')
print('Mi dia estuvo de', resultado)
