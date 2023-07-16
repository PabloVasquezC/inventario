import numpy as np

# FUNCIÓN CONTENEDORA DE EL PROGRAMA DE GESTION DE INVENTARIO
def inventario():
    
    #INVENTARIO INICIAL
    inventario_existente = np.array([["PRODUCTO","CÓDIGO","TIPO","PRECIO","STOCK"],["Martillo","115","Manual","$ 5.000","100"],["Serrucho","045","Manual","$ 5.500","150"],["Atornillador","023","Manual","$ 3.500","200"],["Taladro","015","Electrico","$ 39.990","150"],["Ingleteadora","078","Electrico","$ 230.000","050"],["Lijadora","140","Electrico","$ 50.600","130"]])
    
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
    
    # VALIDACION DE INACAPMAIL
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
        
        
        #INPUT MENU DE OPCIONES
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
            ordenar_por = input("""                                                             VER INVENTARIO POR:
                                
                                
                                                            1.- Orden alfabetico
                                                            2.- Cantidad en Stock 
                                                            --> """)
            
            if ordenar_por == "1":
                
                def bubble_sort_alphabetically(array):
                    n = len(array)
                    for i in range(n - 1):
                        for j in range(n - i - 1):
                            # Comparamos el primer índice de cada lista (el que determina el orden alfabético)
                            if array[j][0] > array[j + 1][0]:
                                # Intercambiamos todas las columnas de las listas utilizando una variable auxiliar
                                temp = np.copy(array[j])
                                array[j] = np.copy(array[j + 1])
                                array[j + 1] = np.copy(temp)

                # Identificamos la primera lista
                first_list = inventario_existente[0]

                # Ordenamos las listas alfabéticamente basándonos en el primer índice
                bubble_sort_alphabetically(inventario_existente[1:])

                # Volvemos a colocar la primera lista en la parte superior
                sorted_inventario = np.vstack((first_list, inventario_existente[1:]))

                # print(sorted_inventario)
                
                inventario_alineado = sorted_inventario.copy()

                # Obtenemos la forma (shape) del array para determinar el número de columnas
                num_filas, num_columnas = sorted_inventario.shape

                # Obtenemos la longitud máxima de cada columna
                longitud_maxima_por_columna = [max(map(len, sorted_inventario[:, i])) for i in range(num_columnas)]

                # Alineamos verticalmente los elementos de cada columna
                for i in range(num_filas):
                    for j in range(num_columnas):
                        inventario_alineado[i, j] = sorted_inventario[i, j].ljust(longitud_maxima_por_columna[j])

                # Convertimos el inventario_alineado en una cadena de texto con formato
                inventario_alineado_str = np.array2string(inventario_alineado, separator=" | ", formatter={'all': lambda x: f"{x}"},)

                # Separamos las líneas del inventario
                lineas = inventario_alineado_str.strip().split("\n")

                # Número de espacios para centrar en una consola de ancho 100
                espacios_para_centar = 90 // 2  # Dividimos por 2 para centrar aproximadamente

                # Creamos el texto con los espacios al principio de cada línea
                inventario_centado = "\n".join(" " * espacios_para_centar + linea for linea in lineas)

                # Imprimimos el texto centrado
                print(" ")
                print(inventario_centado)
                print(" ")
                
        #BUBBLE SORT
        if ordenar_por == "2":
            
            def bubble_sort(array):
                    n = len(array)
                    for i in range(n - 1):
                        for j in range(n - i - 1):
                            # Comparamos el primer índice de cada lista (el que determina el orden alfabético)
                            if array[j][-1] > array[j + 1][-1]:
                                # Intercambiamos todas las columnas de las listas utilizando una variable auxiliar
                                temp = np.copy(array[j])
                                array[j] = np.copy(array[j + 1])
                                array[j + 1] = np.copy(temp)

            # Identificamos la primera lista
            first_list = inventario_existente[0]

            # Ordenamos las listas alfabéticamente basándonos en el primer índice
            bubble_sort(inventario_existente[1:])

            # Volvemos a colocar la primera lista en la parte superior
            sorted_inventario = np.vstack((first_list, inventario_existente[1:]))

            # print(sorted_inventario)
            
            inventario_alineado = sorted_inventario.copy()

            # Obtenemos la forma (shape) del array para determinar el número de columnas
            num_filas, num_columnas = sorted_inventario.shape

            # Obtenemos la longitud máxima de cada columna
            longitud_maxima_por_columna = [max(map(len, sorted_inventario[:, i])) for i in range(num_columnas)]

            # Alineamos verticalmente los elementos de cada columna
            for i in range(num_filas):
                for j in range(num_columnas):
                    inventario_alineado[i, j] = sorted_inventario[i, j].ljust(longitud_maxima_por_columna[j])

            # Convertimos el inventario_alineado en una cadena de texto con formato
            inventario_alineado_str = np.array2string(inventario_alineado, separator=" | ", formatter={'all': lambda x: f"{x}"},)

            # Separamos las líneas del inventario
            lineas = inventario_alineado_str.strip().split("\n")

            # Número de espacios para centrar en una consola de ancho 100
            espacios_para_centar = 90 // 2  # Dividimos por 2 para centrar aproximadamente

            # Creamos el texto con los espacios al principio de cada línea
            inventario_centado = "\n".join(" " * espacios_para_centar + linea for linea in lineas)

            # Imprimimos el texto centrado
            print(" ")
            print(inventario_centado)
            print(" ")
                

         
                
            
        while True:
            seguir_finalizar = input("""                                                        Deseas realizar otra operación?
                                                        
                                                    1.- Si!, Volver al menu de opciones 
                                                    2.- No!, Guardar cambios y cerrar el programa
                                                    --> """)
            
            
            
            if seguir_finalizar == "1":
                break
            
            if seguir_finalizar == "2":
                print(" ")
                print("""                                                         ¡Adios, vuelve pronto!""")
                break
            
            if seguir_finalizar != "1" or seguir_finalizar != "2":
                print(" ")
                print("                                                   ###Opción no valida, intenta otra vez###")
                print(" ")
            
        if seguir_finalizar == "2":
            print(" ")
            break    
            
        #OPCIÓN 2
        if opciones == "2":
            print(" ")
            
            
        #OPCIÓN 3
        if opciones == "3":
            print(" ")
            producto = input("""                                              Ingrese el nombre del producto que deseas agregar al inventario
                                                        --> """) 
            producto = producto.capitalize()
              
            print(" ")
            codigo = input("""                                                Ingresa el código del producto que deseas agregar al inventario
                                                        --> """)
            
            print(" ")
            tipo = input("""                                      Ingresa el tipo de herramienta/material/accesorio que deseas agregar al inventario
                                                        --> """)
            tipo = tipo.capitalize()
            
            nuevo_producto = [producto,codigo,tipo,+1]
            
            inventario_existente = np.append(inventario_existente, nuevo_producto)
            
            print(inventario_existente)
        
        
inventario()
        
        
        