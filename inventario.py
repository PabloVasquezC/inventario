import numpy as np
from datetime import datetime as dt

# FUNCIÓN PRINCIPAL QUE CONTIENE EL PROGRAMA DE GESTION DE INVENTARIO
def inventario():
        
    print(""" ___________________________________
|  SISTEMA DE GESTION DE INVENTARIO |
-------------------------------------""")   
    # VALIDACIÓN USUARIOS
    usuario = input("|  Ingrese su nombre de usuario: ")
    nombre_usuarios = input("Agustin","Cristian","Miguel","Nicolas","Pablo")
    
    contrasena = input("Ingrese la contraseña para acceder al menu de opciones")

    if usuario in nombre_usuarios and contrasena == "inventario1234":
        print()
    
    inventario = np.array([["PRODUCTO","CÓDIGO","TIPO","PRECIO"],["Martillo","115","Manual","5000"],["Serrucho","045","Manual","5500"],["desatornillador","023","Manual","3500"]])
    
    # print(inventario)
    
#     input(""" SISTEMA DE GESTION DE INVENTARIO
# ----------------------------------

# Funciones: 
        
# 1.- Ver inventario.
# 2.-Ver producto.
# 2.- Agregar producto.
# 3.-Quitar producto.

# Ingresa la función que deseas realizar --> """)
    
    
    # def mostrar_inventario():
    #     print(inventario)
        
    def mostrar_producto():
        return 0    
    
        
        
inventario()        
        
        
        