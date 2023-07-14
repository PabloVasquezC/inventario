import numpy as np
from datetime import datetime as dt
import sys

# FUNCIÓN PRINCIPAL QUE CONTIENE EL PROGRAMA DE GESTION DE INVENTARIO
# def inventario():
        
print(""" ___________________________________________________________________________________________________
| 
|  ________    _    ________
| |  ______|  |_|  |  ______|
| | |______    _   | |______
| |______  |  | |  |______  |
|  ______| |  | |   ______| |
| |________|  |_|  |________|
|
-------------------------------------""")   
# VALIDACIÓN USUARIOS


print(f"""|      Ingrese su inacap mail      
    {input("hola")}|""")


contrasena = input("Ingrese la contraseña ")
usuarios_validos = ("agustin.segovia02@inacapmail.cl","cristian.quintanilla08@inacapmail.cl","Miguel","nicolas.riquelme40@inacapmail.cl","pablo.vasquez41@inacapmail.cl") 
    

    # if usuario in usuarios_validos and contrasena == "inventario1234":
    #     print()
    
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
    
        
        
       
        
        
        