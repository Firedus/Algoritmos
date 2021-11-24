#Proyecto Inventario
import time
import datetime

#--------- Variables Globales ---------
autenticado = False

inventario = [
    ["Producto", "Stock", "$", "Ventas"],
    ["Rosas Rojas", 10, 50, 0],
    ["Margaritas", 15, 30, 0],
    ["Tulipanes", 12, 70, 0],
    ["Hortencia", 20, 40, 0],
    ["Orquídea", 8, 90, 0],
    ["Lirio Blanco", 20, 45, 0]
]

carrito = [
    ["Producto","$","Cantidad", "Total"]
]

#--------- Funciones ---------

#Funcion que autentica al usuario para interactuar con el programa LISTO
def inicioSesion():
    usuario = "Jose"
    password = "1234"
    intentos = 0

    while(intentos < 3):
        print("-------------------------------------------------\n")
        print("\t \t INICIO DE SESION \n")
        print("-------------------------------------------------\n")
        print("Ingrese Su Usuario y Contraseña \n")
        usuarioInput = str(input("Usuario: ")) 
        passwordInput = str(input("Contraseña: ")) 
        print("\n")

        if((usuario == usuarioInput) and (password == passwordInput)):
            autenticado = True
            return autenticado
        else:
            print("Los datos proporcionados son incorrectos")
            intentos += 1
    
    if(intentos == 3):
        print("3 intentos fallidos. El inicio de sesión ha sido bloqueado")

#Funcion que pregunta si el usuario quiere seguir comprando LISTO
def seguirComprando():
    print("¿Desea realizar otra operacion? Si / No")
    opcion = input(str())

    if(opcion == "Si"):
        return True
    else:
        exit()

#Funcion para ver el inventario LISTO
def mostrarInventario(array):
    print("\nEste es el inventario actualizado el: ", datetime.datetime.now(), "\n")
    for flor in array:
        print(flor[0],"\t\t",flor[1],"\t\t",flor[2],"\t\t",flor[3])
    print("\n")
    
#Función para agregar, quitar o modificar el inventario LISTO
def modificarInventario():

    while(True):
        print("-------------------------------------------------\n")
        print("\t\tMODIFICAR INVENTARIO \n")
        print("-------------------------------------------------\n")
        print("1 - Agregar")
        print("2 - Eliminar")
        print("3 - Modificar")
        print("Otra - Salir\n")
        opcion = int(input("¿Que desea hacer con el inventario?: "))

        if(opcion == 1):
            print("Decidio agregar un nuevo producto")
            nombre = str(input("Ingrese el nombre del producto: "))
            stock = int(input("Ingrese la cantidad de stock del producto: "))
            precio = int(input("Ingrese el precio (entero) del producto: "))

            nuevoProducto = [nombre, stock, precio, 0]

            inventario.append(nuevoProducto)

            mostrarInventario(inventario)
            return inventario

        elif(opcion == 2):
            print("Decidio eliminar un nuevo producto")
            productoEliminado = str(input("Ingrese el nombre del producto que desea eliminar: "))

            for i in range(0, len(inventario)):
                if(inventario[i][0] == productoEliminado):
                    inventario.pop(i)
                    print("Se eliminó el producto exitosamente")
                    mostrarInventario(inventario)
                    return inventario
            
            print("No se encontró el producto a eliminar, intente de nuevo\n")

        elif(opcion == 3):
            productoModificado = str(input("Ingrese el nombre del producto que desea modificar: "))

            print("\n0 - Nombre")
            print("1 - Stock")
            print("2 - Precio")
            print("Otra - Salir\n")

            columnaModificado = int(input("Ingrese el numero de columna a modificar: "))

            for i in range(0, len(inventario)):
                if(inventario[i][0] == productoModificado):
                    if(columnaModificado == 0):
                        nuevoValor = str(input("Ingrese el nuevo valor del producto: "))
                    elif(columnaModificado == 1 or columnaModificado == 2):
                        nuevoValor = int(input("Ingrese el nuevo valor del producto: "))
                    else:
                        break
                    
                    inventario[i][columnaModificado] = nuevoValor
                    print("Se modifico el producto exitosamente")

                    mostrarInventario(inventario)
                    return inventario
                    
            print("No se encontró el producto a modificar, intente de nuevo \n")
        else:
            break

#Funcion para calcular el total de un carrito LISTO
def totalCarrito(array):
    total = 0

    for i in range (1, len(array)):
        total += array[i][3]

    print("\t\tEl total de su compra es: $", total, "MXN \n")

#Funcion para ejecutar una venta LISTO
def venta():   
    seguir = True
    arregloProducto = []

    while(seguir):
        nombreProducto = str(input(("¿Que producto desea comprar?: ")))
        cantidadProducto = int(input("Ingrese el numero de unidades a comprar: "))
        for i in range(1, len(inventario)):
            if(inventario[i][0] == nombreProducto):
                if(cantidadProducto <= inventario[i][1]):
                    inventario[i][3] += cantidadProducto
                    inventario[i][1] -= cantidadProducto
                    total = cantidadProducto * inventario[i][2]
                    arregloProducto = [inventario[i][0], inventario[i][2], cantidadProducto, total]
                    carrito.append(arregloProducto)
                    print("\n",inventario[i][0], "agregado al carrito exitosamente")
                else:
                    print("No hay suficientes unidades de este producto, intente de nuevo")
        
        opcion = str(input("\n¿Desea comprar otro articulo? Si / No : "))
        if(opcion == "Si"):
            seguir = True
        else:
            break 

    return carrito

#Funcion para ver el carrito de compras LISTO
def verCarrito(array):
    print("\nEste es el carrito actualizado el: ", datetime.datetime.now(), "\n")
    for producto in array:
        print(producto[0],"\t\t",producto[1],"\t\t",producto[2],"\t\t",producto[3])
    print("\n")

    totalCarrito(array)

#Funcion que muestra el producto mas vendido LISTO
def masVendido():
    valorVenta = inventario[1][3]
    indiceMayor = 1

    for i in range (1, len(inventario)):
        if(inventario[i][3] > valorVenta):
            valorVenta = inventario[i][3]
            indiceMayor = i

    producto = inventario[indiceMayor][0]
    ventas = inventario[indiceMayor][3]
    print("El producto más vendido es: ", producto," con ", ventas ," ventas\n")

#Funcion que muestra el producto menos vendido LISTO
def menosVendido():
    valorVenta = inventario[1][3]
    indiceMenor = 1

    for i in range (1, len(inventario)):
        if(inventario[i][3] < valorVenta):
            valorVenta = inventario[i][3]
            indiceMenor = i

    producto = inventario[indiceMenor][0]
    ventas = inventario[indiceMenor][3]
    print("El producto menos vendido es: ", producto," con ", ventas ," ventas\n")

#Funcion que muestra el total de ganancias LISTO
def totalVentas():
    total = 0

    mostrarInventario(inventario)

    for i in range (1, len(inventario)):
        totalProducto = inventario[i][3] * inventario[i][2]
        total += totalProducto
    print("El total de ventas fue de: $", total, "MXN \n")
    
#Funcion que muestra el total de stock LISTO
def totalStock():
    total = 0

    mostrarInventario(inventario)

    for i in range (1, len(inventario)):
        total += inventario[i][1]

    print("El total de Stock es de: ", total, "unidades")

#--------- Interfaz de Usuario ---------

# Si se autentica el usuario, inicia el Menu
if(inicioSesion()):
    while(True):
        #Menu
        print("-------------------------------------------------\n")
        print("\tInventario de Flores en Monterrey \n")
        print("-------------------------------------------------")
        time.sleep(1)
        print("\n \t \t MENU DE OPCIONES \n")
        time.sleep(1)
        print("1 - Ver Inventario")
        print("2 - Modificar Inventario")
        print("3 - Venta")
        print("4 - Ver Carrito de Compras")
        print("5 - Producto Mas Vendido")
        print("6 - Producto Menos Vendido")
        print("7 - Total de Ventas")
        print("8 - Total de Stock")
        print("0 - Salir \n")
        print("-------------------------------------------------")
        time.sleep(1)

        opcion = int(input("\nIngrese la operación a realizar: "))

        #Seleccion de funcion y ejecucion
        if(opcion == 1):
            print("Ingresó la opción 'Ver Inventario' \n")
            mostrarInventario(inventario)
            seguirComprando()
        elif(opcion == 2):
            print("Ingresó la opción 'Modificar Inventario' \n")
            modificarInventario()
            seguirComprando()
        elif(opcion == 3):
            print("Ingresó la opción 'Venta' \n")
            carrito = venta()
            seguirComprando()
        elif(opcion == 4):
            print("Ingresó la opción 'Ver Carrito de Compras' \n")
            verCarrito(carrito)
            seguirComprando()
        elif(opcion == 5):
            print("Ingresó la opción 'Producto Mas Vendido' \n")
            masVendido()
            seguirComprando()
        elif(opcion == 6):
            print("Ingresó la opción 'Producto Menos Vendido' \n")
            menosVendido()
            seguirComprando()
        elif(opcion == 7):
            print("Ingresó la opción 'Total de Ventas' \n")
            totalVentas()
            seguirComprando()
        elif(opcion == 8):
            print("Ingresó la opción 'Total de Stock' \n")
            totalStock()
            seguirComprando()
        elif(opcion == 0):
            print("\nSaliendo... \n") 
            exit()
        else:
            print("Ingrese una opción válida")




