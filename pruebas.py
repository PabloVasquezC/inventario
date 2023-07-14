validacion_mail = input("--> ")

# Dimensiones del rectángulo
ancho = 30
alto = 5

# Dibujar el rectángulo con el input
print('+' + '-' * (ancho - 2) + '+')
for _ in range(alto - 2):
    print('|' + ' ' * (ancho - 2) + '|')
print('|' + f'       {validacion_mail}{" " * (ancho - 11)}' + '|')
for _ in range(alto - 2):
    print('|' + ' ' * (ancho - 2) + '|')
print('+' + '-' * (ancho - 2) + '+')