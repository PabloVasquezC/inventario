import numpy as np

#INTEGRANTES PROYECTO: PABLO VASQUEZ, CRISTIAN QUINTANILLA, AGUSTIN SEGOVIA, NICOLAS RIQUELME

# FUNCIÓN CONTENEDORA DEL PROGRAMA DE GESTION DE INVENTARIO
def gestiona_inventario(inventario):
    
    #TIPOGRAFIA INICIO
    print("""                  ________    _    ________    _________    ________    __    __    ________         _______     ________
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
    # BUCLE DE VALIDACION DE INACAPMAIL
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
            print("""                                              la contraseña es incorrecta, intente nuevamente
                  """)
            
        if validacion_contrasena == "inventario1234":
            print(" ")
            break
    
    
    #MENU DE OPCIONES
    bandera_mayor = True
    while bandera_mayor:
    
        #INPUT MENU DE OPCIONES
        print(" ")
        opciones = input("""                                                                OPCIONES
                                                               ----------
            
                                                          1.- Ver inventario.
                                                          2.- Buscar producto(s).
                                                          3.- Agregar producto.
                                                          4.- Eliminar producto.
                                                          5.- Modificar producto.
                                                          6.- Cerrar programa.

                                                  Ingresa la función que deseas realizar 
                                                  --> """)
        
        #OPCIÓN 1 -VER INVENTARIO
        if opciones == "1" :
            print(" ")
            #INPUT ALGORITMO DE ORDENAMIENTO
            while True:
                ordenar_por = input("""                                                             VER INVENTARIO POR:
                                    
                                                        1.- Ver inventario por orden alfabetico
                                                        2.- Ver inventario por cantidad en Stock 
                                                        --> """)
                
                #ORDENAMIENTO BURBUJA
                if ordenar_por == "1":
                    
                    def ordenamiento_burbuja(array):
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
                    first_list = inventario[0]

                    # Ordenamos las listas alfabéticamente basándonos en el primer índice
                    ordenamiento_burbuja(inventario[1:])

                    # Volvemos a colocar la primera lista en la parte superior
                    sorted_inventario = np.vstack((first_list, inventario[1:]))

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
                    break
                    
            
                #ORDENAMIENTO POR INSERSION
                if ordenar_por == "2":
                
                    def ordenamiento_por_insercion(array):
                        n = array.shape[0]
                        for i in range(1, n):
                            # Guardamos el elemento actual en una variable temporal
                            current_element = np.copy(array[i])
                            # Inicializamos un índice para comparar con los elementos anteriores
                            j = i - 1

                            # Desplazamos los elementos mayores que el actual hacia adelante
                            # hasta encontrar la posición correcta para insertar el elemento actual
                            while j >= 0 and current_element[-1] < array[j][-1]:
                                array[j + 1] = np.copy(array[j])
                                j -= 1

                            # Insertamos el elemento actual en su posición correcta
                            array[j + 1] = np.copy(current_element)

                    #TRANSFORMANDO EL NP.ARRAY A TEXTO PARA POSISIONARLO AL CENTRO DE LA CONSOLA                
                    # Identificamos la primera lista
                    first_list = inventario[0]

                    # Ordenamos las listas alfabéticamente basándonos en el primer índice
                    ordenamiento_por_insercion(inventario[1:])

                    # Volvemos a colocar la primera lista en la parte superior
                    sorted_inventario = np.vstack((first_list, inventario[1:]))

                    
                    
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
                    break
                    
                if ordenar_por not in ["1","2"]:
                        print("""                                                                       
                                                    Opción  invalida, intenta otra vez
                                                                                                """)
                
            #PREGUNTANDO POR CONTINUIDAD O CIERRE DEL PROGRAMA
            while True:
                seguir_finalizar = input("""                                                        Deseas realizar otra operación?
                                                            
                                                        1.- Si!, Volver al menu de opciones 
                                                        2.- No!, Guardar cambios y cerrar el programa
                                                        --> """)
                
                
                
                if seguir_finalizar == "1":
                    opciones = "1"
                    break
                
                if seguir_finalizar == "2":
                    print(" ")
                    print("""                                                         ¡Adios, vuelve pronto!""")
                    bandera_mayor = False
                    break
                
                if seguir_finalizar != "1" or seguir_finalizar != "2":
                    print(" ")
                    print("                                                   ###Opción invalida, intenta otra vez###")
                    print(" ")
        
        #OPCIÓN 2 -BUSCAR PRODUCTO(S)
        if opciones == "2":
            
            print(" ")
            tipo_busqueda = input("""                                                         DESEAS BUSCAR PRODUCTO(S) POR:
        
                                                                1.- Nombre
                                                                2.- Código
                                                                3.- Precio
                                                                --> """)
        
        
            #DEFINIENDO FUNCIÓN DE BUSQUEDA LINEAL
            def buscar_nombre_en_lista(lista_de_listas, nombre_buscado):
                for lista in lista_de_listas:
                    if nombre_buscado in lista:
                        print(" ")
                        print(f"""                                                    {inventario_ferreteria[0]}          
                                                    {lista}""")
                        print(" ")
                return None  
        
        
            #BUSCANDO PRODUCTO POR NOMBRE   
            if tipo_busqueda == "1":
                while True:
                    print(" ")
                    nombre = input("""                                                     Ingrese el nombre del producto que desea buscar
                                                            --> """)
                
                    nombre = nombre.capitalize()
                
                    if nombre in inventario_ferreteria:
                        buscar_nombre_en_lista(inventario_ferreteria, nombre)
                        break 
                    
                    if nombre not in inventario_ferreteria:
                        print(" ")
                        print("""                                                     Al parecer el producto que deseas buscar no 
                                                        se encuentra en el inventario, intenta otra vez
                                                            """)    
            
            #BUSCANDO PRPDUCTO POR CÓDIGO
            if tipo_busqueda == "2":
                print(" ")
                while True:
                    codigo = input("""                                                     Ingrese el código del producto que desea buscar
                                                        --> """)
                    
                    
                    if codigo in inventario_ferreteria:
                        buscar_nombre_en_lista(inventario_ferreteria, codigo)
                        break   
                    print(" ")
                    print("""                                                     Al parecer el producto que deseas buscar no 
                                                        se encuentra en el inventario, intenta otra vez
                                                        """) 
                    break
            if tipo_busqueda == "3":
                print(" ")    
                while True:
                    precio = input("""                                                     Ingrese el precio del producto que desea buscar
                                                        --> """)
                    precio = "$ "+ precio     
                    
                    if precio in inventario_ferreteria:
                        buscar_nombre_en_lista(inventario_ferreteria, precio)
                        break   
                    print(" ")
                    print("""                                                     Al parecer el producto que deseas buscar no 
                                                        se encuentra en el inventario, intenta otra vez
                                                        """) 
                    break
            if tipo_busqueda not in ["1","2","3"]:
                print("""
                                                        Opción invalida, intenta otra vez
                                                        """)       
                
                #PREGUNTANDO POR CONTINUIDAD O CIERRE DEL PROGRAMA
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
                                
        #OPCIÓN 3 -AGREGAR PRODUCTO           
        if opciones == "3":
              
            while True: 
                print(" ")
                nuevo_producto = input("""                                                         Ingrese el nombre del producto 
                                                        que desea agregar al inventario
                                                        --> """)
                nuevo_producto = nuevo_producto.capitalize()
                if len(nuevo_producto) == 0:
                    print("""                                       
                                                    ###Ingresa almenos una letra para guardar 
                                                        el nombre detu nuevo producto###""")
                if len(nuevo_producto) > 0:
                    break    
            
            print(" ")
            nuevo_codigo = input("""                                                         Ingrese el código del producto
                                                        que desea agregar al inventario
                                                        --> """)
            nuevo_codigo = nuevo_codigo.capitalize()
            
            while True:
                print(" ")
                nuevo_tipo = input("""                                                         Ingresa el tipo del producto
                                                        que deseas agregar al inventario
                                                        --> """)
                nuevo_tipo = nuevo_tipo.capitalize()
                if len(nuevo_tipo) == 0:
                    print("""                                       
                                                        ###Ingresa almenos un tipo de producto 
                                                        para guardar tu nuevo producto###""")
                if len(nuevo_tipo) > 0:
                    break    
            
            while True:
                try:
                    print(" ")
                    nuevo_precio = int(input("""                                                     Ingresa sin puntos el precio del 
                                                producto que deseas agregar al inventario                                            
                                                        --> """))
                    
                    if nuevo_precio <= 0:
                        print("                                                   ####Lo sentimos, debes ingresar valores positivos###")
                    
                    if nuevo_precio > 0 :
                        signo_peso = "$ "
                        
                        nuevo_precio = str(nuevo_precio)
                        mezcla = str(signo_peso + nuevo_precio)
                        
                        break                        
                except ValueError:
                    print("                                                                       ####Lo sentimos, debes ingresar valores positivos###")
            
            while True:
                try:        
                    nuevo_stock = int(input("""                                                        Ingrese el stock del producto
                                                        que desea agregar al inventario
                                                        --> """))
                    if nuevo_stock < 0:
                        print("                                                                       ####Lo sentimos, debes ingresar valores positivos###")
                    
                    if nuevo_stock > 0:
                        nuevo = ([nuevo_producto,nuevo_codigo,nuevo_tipo,mezcla,nuevo_stock])
                        inventario = np.vstack((inventario, nuevo))
                        print("""                                                                            
                                                    El producto fue ingresado con exito
                                """)
                        break    
                    break
                except ValueError:
                    print("                                                                       ####Lo sentimos, debes ingresar valores positivos###")

            
            ##PREGUNTANDO POR CONTINUIDAD
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

        #OPCIÓN 4 -QUITAR PRODUCTO
        if opciones == "4":
            bandera_4 = True
            while bandera_4:
                print(" ")
                eliminar_por = input("""                                                           Eliminar producto por:
                                        
                                                                1.- Nombre
                                                                2.- Código
                                                                
                                                                --> """)
                
                    #DEFINIENDO FUNCIÓN DE BUSQUEDA LINEAL 
                def buscar_nombre_en_lista(lista_de_listas, nombre_buscado):
                    for lista in lista_de_listas:
                        if nombre_buscado in lista:
                            print(" ")
                            print(f"""                                                    {inventario_ferreteria[0]}          
                                                    {lista}""")
                            print(" ")
                    return None  
            
            
                #BUSCANDO PRODUCTO POR NOMBRE   
                if eliminar_por == "1":
                    bandera = True
                    while bandera:
                        print(" ")
                        nombre = input("""                                                 Ingrese el nombre del producto que desea eliminar
                                                        --> """)
                    
                        nombre = nombre.capitalize()
                    
                        if nombre in inventario:
                            print(" ")
                            print("""                                                    El producto a eliminar es el siguente: 
                                                """)
                            buscar_nombre_en_lista(inventario, nombre) 
                            print(" ")
                            while True:
                                decision = input("""                                                    Confirmar eliminación:
                                                                    1.-Si
                                                                    2.-No
                                                                    -->""")
                                if decision == "1":
                                    # Buscar el índice del artículo en el inventario
                                    indice_articulo = np.where(inventario[:, 0] == nombre)

                                    if len(indice_articulo[0]) > 0:
                                        # Si el artículo existe, eliminarlo del inventario
                                        inventario = np.delete(inventario, indice_articulo, axis=0)                            
                                        print("""
                                                        El producto ha sido eliminado con éxito
                                                """)
                                        bandera = False
                                        bandera_4 = False
                                        break
                                        
                                    if decision == "2":
                                        print("Opción invalida, intenta otra vez")
                                    
                
                #BUSCANDO PRODUCTO POR NOMBRE   
                if eliminar_por == "2":
                    bandera = True
                    while bandera:
                        print(" ")
                        codigo = input("""                                                 Ingrese el código del producto que desea eliminar
                                                        --> """)
                    
                        codigo = codigo.capitalize()
                    
                        if codigo in inventario:
                            print(" ")
                            print("""                                                    El producto a eliminar es el siguente: 
                                                """)
                            buscar_nombre_en_lista(inventario, codigo) 
                            print(" ")
                            while True:
                                decision = input("""                                                    Confirmar eliminación:
                                                                    1.-Si
                                                                    2.-No
                                                                    --> """)
                                if decision == "1":
                                    # Buscar el índice del artículo en el inventario
                                    indice_articulo = np.where(inventario[:, 1] == codigo)

                                    if len(indice_articulo[0]) > 0:
                                        # Si el artículo existe, eliminarlo del inventario
                                        inventario = np.delete(inventario, indice_articulo, axis=0)
                                        print("""
                                            El producto ha sido eliminado con éxito
                                            """)
                                        bandera = False
                                        bandera_4 = False
                                        break
                                        
                                if decision == "2":
                                    print("Opción invalida, intenta otra vez")
                                
                if eliminar_por not in ["1","2"]:
                    print(" ")
                    print("                                                    ###Opcion invalida, intenta otra vez###")            
                    print(" ")
            #PREGUNTANDO POR CONTINUIDAD O CIERRE DEL PROGRAMA
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

        #OPCIÓN 5 -MODIFICAR PRODUCTO
        if opciones == "5":
            print(" ")
            modificar_por = input("""                                                      Buscar el producto a modificar por:
                                  
                                                        1.- Nombre
                                                        2.- Código
                                                        --> """)
                
                #DEFINIENDO FUNCIÓN DE BUSQUEDA LINEAL 
            def buscar_nombre_en_lista(lista_de_listas, nombre_buscado):
                for lista in lista_de_listas:
                    if nombre_buscado in lista:
                        print(" ")
                        print(f"""                                                    {inventario_ferreteria[0]}          
                                                    {lista}""")
                        print(" ")
                return None  
          
        
            #BUSCANDO PRODUCTO POR NOMBRE   
            if modificar_por == "1":
                while True:
                    print(" ")
                    nombre = input("""                                                 Ingrese el nombre del producto que desea modificar
                                                    --> """)
                
                    nombre = nombre.capitalize()
                    
                
                    if nombre in inventario_ferreteria:
                        print(" ")
                        print("""                                                    El producto a modificar es el siguente: 
                                             """)
                        buscar_nombre_en_lista(inventario_ferreteria, nombre) 
                        print(" ")
                        
                    # Buscar el índice del producto en el inventario
                    indice_producto = np.where(inventario_ferreteria[:, 0] == nombre)

                    if len(indice_producto[0]) > 0:
                        # Si el producto existe, obtener los nuevos campos del usuario mediante inputs
                        nuevo_nombre = input("""                                                      Ingrese el nuevo nombre del producto
                                                      --> """)
                        nuevo_codigo = input("""                                                      Ingrese el nuevo código del producto
                                                      --> """)
                        nuevo_tipo = input("""                                                        Ingrese el nuevo tipo del producto
                                                      --> """)
                        while True:
                            nuevo_precio = input("""                                                      Ingrese el nuevo precio del producto
                                                      --> """)
                            nuevo_precio = int(nuevo_precio)
                            if nuevo_precio > 0:
                                nuevo_precio = str(nuevo_precio)
                                break
                            
                            if nuevo_precio <= 0:
                                print("""                                         
                                      Opcion invalida, debes ingresar valores positivos, intenta otra vez
                                      """)
                                
                        nuevo_stock = input("""                                                       Ingrese el nuevo stock del producto 
                                                      --> """)

                        # Actualizar los campos del producto existente
                        inventario_ferreteria[indice_producto, 0] = nuevo_nombre
                        inventario_ferreteria[indice_producto, 1] = nuevo_codigo
                        inventario_ferreteria[indice_producto, 2] = nuevo_tipo
                        inventario_ferreteria[indice_producto, 3] = "$ " + nuevo_precio
                        inventario_ferreteria[indice_producto, 4] = nuevo_stock

                        print(" ")
                        print("                                                       Inventario actualizado con exito")
                        print("")
                        # print(inventario_ferreteria)
                        break

                     
                    if nombre not in inventario_ferreteria:
                        print(" ")
                        print("""                                                     Al parecer el producto que deseas buscar no 
                                                        se encuentra en el inventario, intenta otra vez
                                                            """)    
            
            #BUSCANDO PRPDUCTO POR CÓDIGO
            if modificar_por == "2":
                print(" ")
                while True:
                    codigo = input("""                                                     Ingrese el código del producto que desea buscar
                                                                        --> """)
                    
                    
                    if codigo in inventario_ferreteria:
                        buscar_nombre_en_lista(inventario_ferreteria, codigo)
                        break   
                    print(" ")
                    print("""                                                     Al parecer el producto que deseas buscar no 
                                                        se encuentra en el inventario, intenta otra vez
                                                        """)    
                
            #PREGUNTANDO POR CONTINUIDAD O CIERRE DEL PROGRAMA
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
                
        #OPCIÓN 6 -CERRAR PROGRAMA
        if opciones == "6":
            print("")
            print("                                                        ¡Adios, vuelve pronto!")
            break
     
        if opciones not in ["1","2","3","4","5","6"]:
            print(" ")
            print("                                                  ###Opción invalida, intenta otra vez###")
        
        
#INVENTARIO INICIAL
inventario_ferreteria = np.array([["PRODUCTO","CÓDIGO","TIPO","PRECIO","STOCK"],["Martillo","107","Manual","$ 5000","100"],["Serrucho","109","Manual","$ 5500","150"],["Atornillador","100","Manual","$ 3500","200"],["Taladro","105","Electrico","$ 39990","150"],["Ingleteadora","101","Electrico","$ 230000","050"],["Lijadora","104","Electrico","$ 50600","130"],["Esmeril","106","Electrico","$ 230000","050"]])


# PARA EFECTOS DE UNA BUENA VISIBILIDAD DE LA EJECUCIÓN DEL PROGRAMA EN LA CONSOLA SIGUE ESTOS DOS PASOS:
# 1-MINIMIZAR LA BARRA DE NAVEGACIÓN A TU IZQUIERDA (Ctrl+Shift+E)   
# 2-AGRANDAR LA CONSOLA HASTA QUE ESTA OCUPE TODA LA PANTALLA (Ctrl+ñ) SEGUIDO DE..EHH..AGRANDAR LA CONSOLA AL MAXIMO XD    
gestiona_inventario(inventario_ferreteria)
        
        
        