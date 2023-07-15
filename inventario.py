import numpy as np

# FUNCIÓN CONTENEDORA DE EL PROGRAMA DE GESTION DE INVENTARIO
def inventario():
    inventario_existente = np.array([["PRODUCTO","CÓDIGO","TIPO","PRECIO"],["Martillo","115","Manual","$ 5.000"],["Serrucho","045","Manual","$ 5.500"],["desatornillador","023","Manual","$ 3.500"],["Taladro","015","Electrico","$ 39.990"],["Ingleteadora","078","Electrico","$ 230.000"],["Lijadora","140","Electrico","$ 50.600"]])
    
   
    
    
    
    #TIPOGRAFIA INICIO
    print("""                 ________    _    ________    _________    ________    __    __    ________         _______     ________
                |  ______|  |_|  |  ______|  |___   ___|  |  ______|  |  \\__/  |  |  ____  |       |  ____ \\   | _______|
                | |______    _   | |______       | |      | |______   |        |  | |____| |       | |    \\ |  | |______
                |______  |  | |  |______  |      | |      |  ______|  | |\\__/| |  |  ____  |       | |    | |  |  ______|
                 ______| |  | |   ______| |      | |      | |______   | |    | |  | |    | |       | |____/ |  | |______
                |________|  |_|  |________|      |_|      |________|  |_|    |_|  |_|    |_|       |_______/   |________|
                 ________    ________    ________    _________    _    ________    __   __         _______     ________
                |  ______|  |  ______|  | _______|  |___   ___|  |_|  |  ____  |  |  \\ |  |       |  ____ \\   | _______|
                | |   ___   | |______   | |______       | |       _   | |    | |  |   \\|  |       | |    \\ |  | |______
                | |  |_  |  |  ______|  |______  |      | |      | |  | |    | |  |       |       | |    | |  |  ______|
                | |____| |  | |______    ______| |      | |      | |  | |____| |  |  |\\   |       | |____/ |  | |______
                |________|  |________|  |________|      |_|      |_|  |________|  |__| \\__|       |_______/   |________|
                 _    __   __  __        __  ________    __   __    _________    ________    ________    _    ________
                |_|  |  \\ |  | \\ \\      / / |  ______|  |  \\ |  |  |___   ___|  |  ____  |  |  ____  |  |_|  |  ____  |
                 _   |   \\|  |  \\ \\    / /  | |______   |   \\|  |      | |      | |____| |  | |____|_|   _   | |    | |
                | |  |       |   \\ \\  / /   |  ______|  |       |      | |      |  ____  |  |  ____|_   | |  | |    | |
                | |  |  |\\   |    \\ \\/ /    | |______   |  |\\   |      | |      | |    | |  | |    | |  | |  | |____| |
                |_|  |__| \\__|     \\__/     |________|  |__| \\__|      |_|      |_|    |_|  |_|    |_|  |_|  |________|
                        """)   

    
    # VALIDACIÓN USUARIOS
    
    #BUCLE DE VALIDACION DE INACAPMAIL
    while True:
        usuarios_validos = ["agustin.segovia02@inacapmail.cl","cristian.quintanilla08@inacapmail.cl","miguel.chacana@inacapmail.cl","nicolas.riquelme40@inacapmail.cl","pablo.vasquez41@inacapmail.cl"] 
        usuario = input("""                                                         Ingrese su inacapmail                   
                                                         --> """)
        if usuario not in usuarios_validos:
            print(" ")
            print("                                        ###Lo sentimos, su inacapmail no esta registrado, intente otra vez###        ")
            print(" ")
        if usuario in usuarios_validos:
            print(" ")
            break
     
    #BUCLE DE VALIDACIÓN DE CONTRASEÑA    
    while True:
        validacion_contrasena = input("""                                                         Ingrese su contraseña
                                                         --> """)
        if validacion_contrasena != "inventario1234":
            print(" ")
            print("                                               la contraseña es incorrecta, intente nuevamente")
            
        if validacion_contrasena == "inventario1234":
            print(" ")
            break
        




    
    
    

        return 0
    # print(inventario)
    
    #MENU DE OPCIONES
    while True:
        opciones = input("""                                                                OPCIONES
                                                              ----------
            
                                                            1.- Ver inventario.
                                                            2.- Ver producto(s).
                                                            3.- Agregar producto.
                                                            4.- Quitar producto.

                                                        Ingresa la función que deseas realizar 
                                                        --> """)
        
        #OPCIÓN 1
        if opciones == "1" :
            print(" ")
            # OBTENIENDO LA LONGITUD MAXIMA DE CADA COLUMNA
            ancho_columnas = np.vectorize(len)(inventario_existente).max(axis=0)

            # IMPRESION ALINEADA DE MATRIZ
            for fila in inventario_existente:
                fila_alineada = [element.ljust(width) for element, width in zip(fila, ancho_columnas)]
                print(f'                                                     {"   ".join(fila_alineada)}')
                print(" ")
            
            while True:
                seguir_finalizar = input("""                                                        Deseas realizar otra operación?
                                                            
                                                        1.- Si!, Volver al menu de opciones 
                                                        2.- No!, Guardar cambios y cerrar el programa
                                                        --> """)
                if seguir_finalizar != "1" or seguir_finalizar != "2":
                    print(" ")
                    print("                                                   ###Opción no valida, intenta otra vez###")
                    print(" ")
                
                if seguir_finalizar == "1":
                    break
                
                if seguir_finalizar == "2":
                    print(" ")
                    print("""                                                          ¡Adios, vuelve pronto!""")
                    break
                
                
        
        if seguir_finalizar == "2":
            break    
        
        #OPCIÓN 2
        if opciones == "2":
            
            eleccion = input("""                                          Ingrese el nombre del producto
                                                            -->""")
            eleccion = eleccion.capitalize()
        
        #OPCIÓN 3
        if opciones == "3":
            return 0
        
        #OPCIÓN 4
        if opciones == "4":
            return 0
        
        
        if opciones != "1" or opciones != "2" or opciones != "3" or opciones != "4":
            print(" ")
            print("                                                        ###Opcion invalida, intenta otra vez###")
            print(" ")
            
        
        
        
        
    
    
        
inventario()
        
        
        