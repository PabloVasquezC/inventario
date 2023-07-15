import numpy as np

# FUNCIÓN CONTENEDORA DE EL PROGRAMA DE GESTION DE INVENTARIO
def inventario():
    inventario_existente = np.array([["PRODUCTO","CÓDIGO","TIPO","PRECIO","STOCK"],["Martillo","115","Manual","$ 5.000","100"],["Serrucho","045","Manual","$ 5.500","150"],["Atornillador","023","Manual","$ 3.500","200"],["Taladro","015","Electrico","$ 39.990","150"],["Ingleteadora","078","Electrico","$ 230.000","50"],["Lijadora","140","Electrico","$ 50.600","130"]])
    
    
    
    # Copiamos el inventario_existente en otra variable
    inventario_alineado = inventario_existente.copy()

    # Obtenemos la forma (shape) del array para determinar el número de columnas
    num_filas, num_columnas = inventario_existente.shape

    # Obtenemos la longitud máxima de cada columna
    longitud_maxima_por_columna = [max(map(len, inventario_existente[:, i])) for i in range(num_columnas)]

    # Alineamos verticalmente los elementos de cada columna
    for i in range(num_filas):
        for j in range(num_columnas):
            inventario_alineado[i, j] = inventario_existente[i, j].ljust(longitud_maxima_por_columna[j])

    # Convertimos el inventario_alineado en una cadena de texto con formato
    inventario_alineado_str = np.array2string(inventario_alineado, separator=" | ", formatter={'all': lambda x: f"{x}"},)
    
  
    print(inventario_alineado_str) 
    
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
            
            #ALGORITMOS DE ORDENAMIENTO
            ordenar_por = input("""                                                             Ver inventario por:
                                
                                
                                                            1.- Orden alfabetico
                                                            2.- Cantidad en Stock 
                                                            --> """)
            
            if ordenar_por == "1":
                
                def bubble_sort(arr, key_idx):
                    n = len(arr)
                    for i in range(n):
                        for j in range(0, n-i-1):
                            # Comparamos los elementos del array según el índice especificado por key_idx
                            if arr[j][key_idx] > arr[j+1][key_idx]:
                                arr[j], arr[j+1] = arr[j+1], arr[j]

                # Creamos una copia del inventario para mantener el original intacto
                inventario_ordenado = inventario_existente.copy()

                # Obtenemos la lista de productos a ordenar
                productos_a_ordenar = inventario_ordenado[1:]

                # Ordenamos el inventario alfabéticamente por el nombre del producto (segunda columna)
                bubble_sort(productos_a_ordenar, key_idx=0)

                # Concatenamos la cabecera (primera fila) con las filas ordenadas
                inventario_ordenado[1:] = productos_a_ordenar

                # Convertimos el inventario_ordenado en una cadena de texto con formato
                inventario_ordenado_str = np.array2string(inventario_ordenado, separator=" | ", formatter={'all': lambda x: f"{x}"},)

                print("Inventario original:")
                print(inventario_existente)

                print("\nInventario ordenado con Bubble Sort:")
                print(inventario_ordenado_str)







            
           






  
            
            
            
            
            # while True:
            #     seguir_finalizar = input("""                                                        Deseas realizar otra operación?
                                                            
            #                                             1.- Si!, Volver al menu de opciones 
            #                                             2.- No!, Guardar cambios y cerrar el programa
            #                                             --> """)
                
                
                
            #     if seguir_finalizar == "1":
            #         break
                
            #     if seguir_finalizar == "2":
            #         print(" ")
            #         print("""                                                         ¡Adios, vuelve pronto!""")
            #         break
                
            #     if seguir_finalizar != "1" or seguir_finalizar != "2":
            #         print(" ")
            #         print("                                                   ###Opción no valida, intenta otra vez###")
            #         print(" ")
                
            # if seguir_finalizar == "2":
            #     print(" ")
            #     break    
        
        #OPCIÓN 2
        if opciones == "2":
            print(" ")
            tipo_busqueda = input()
            
            
            
            # print(" ")
            # eleccion = input("""                                                         Ingrese el nombre del producto
            #                                             --> """)
            # eleccion = eleccion.capitalize()
            
            # productos_coincidentes = []
            
            
            # for producto in range(1, inventario_existente):
            #     if eleccion == producto[0]:
            #         productos_coincidentes = productos_coincidentes.append(productos_coincidentes)
                
            # print(productos_coincidentes)
        
        
        
        
inventario()
        
        
        