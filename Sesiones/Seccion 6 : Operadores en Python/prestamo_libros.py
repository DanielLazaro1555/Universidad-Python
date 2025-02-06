print('*** Sistema Prestamo de Libros ***')
DISTANCIA_PERMITIDA_kM = 3
tiene_credencial = input('¿Cuentas con credencial de estudiante? (Si/No) ')
distancia_biblioteca_km = int(
    input('¿A cuántos kilómetros vives de la Biblioteca? '))  # 1

es_elegible_prestamo = tiene_credencial.strip().lower(
) == 'si' or distancia_biblioteca_km <= DISTANCIA_PERMITIDA_kM


print(f'¿Eres elegible para el préstamo de libros? {es_elegible_prestamo}')
