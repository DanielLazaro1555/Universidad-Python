# *** Sistema Tienda Online ***
#
# Crear el detalle de un producto de una tienda online.
#
# El detalle del producto debe tener:
#   - Nombre del producto
#   - Precio del producto
#   - Cantidad en el inventario
#   - Indicar si está disponible
#
# Hacer algunos cambios y mandar a imprimir nuevamente el nuevo valor de las variables.
#
# El resultado debe ser similar al siguiente:
#
# *** Sistema de Tienda Online ***
# Producto: Cámara digital
# Precio: $399.99
# Cantidad inventario: 20
# Disponible: True

print('*** Sistema de Tienda Online ***')
# Definimos las variables de un producto
nombre_producto = 'Cámara digital'
precio_producto = 399.99
cantidad_inventario = 20
disponible_entrega = True
print('Producto:', nombre_producto)
print('Precio:', precio_producto)
print('Cantidad inventario:', cantidad_inventario)
print('Disponible:', disponible_entrega)

# Hacemos algunos cambios
precio_producto = 299.99
cantidad_inventario = 10
disponible_entrega = True

# MOstrar informacion del producto
print('****************************************************')
print('Producto:', nombre_producto)
print('Precio:', precio_producto)
print('Cantidad inventario:', cantidad_inventario)
print('Disponible para entrega:', disponible_entrega)
