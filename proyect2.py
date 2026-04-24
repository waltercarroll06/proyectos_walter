menu = {
    "hamburguesa": 15000,
    "pizza": 20000,
    "perro": 10000,
    "gaseosa": 5000,
    "papas": 7000
    }

pedidos = []
def mostrar_menu(menu):
    print(menu)

def agregar_producto(pedidos):
    # menu
    for index , i in enumerate(menu , 1 ):
        print(f"{index}. {i}")

    #inputs 

    pedido = input("ingresa el producto que desea: ")
    #condiciones
    if pedido not in menu:
        raise ValueError("producto invalido")
    
    correcto = True
    while correcto:
        try:
            cantidad = int(input("ingresa la cantidad que desea: "))
            if cantidad < 0:
                print("numero invalido")
            else:
                correcto = False
        except ValueError:
            print("error ingrese solo la cantidad")
    
    pedidos.append({
        "pedido": pedido,
        "cantidad": cantidad
    })
        
def calcular_total(pedidos):
    cantidad = 0
    for items in pedidos:
        cantidad += items["cantidad"]
    print("cantidad de productos: " , cantidad , "valor final por producto: \n")
    total_por_producto = 0
    total_general = 0
    for porducto in pedidos:
        nombre = porducto["pedido"]
        cantidad_por_producto = porducto["cantidad"]
        precio = menu[nombre]
        sub_total = cantidad_por_producto * precio
        print(f"{nombre} x{cantidad_por_producto}: {sub_total}")
        total_general += sub_total
    print("Total a pagar:", total_general)
    
    
while True:
    print("\n====================")
    print("     PEDIDOS APP")
    print("====================")
    print("1) Ver menú")
    print("2) Agregar producto")
    print("3) Ver total")
    print("4) Cancelar pedido")
    print("5) Salir")
    print("====================")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_menu(menu)

    elif opcion == "2":
        try:
            agregar_producto(pedidos)
        except ValueError as e:
            print(e)

    elif opcion == "3":
        if not pedidos:
            print("No hay pedidos")
        else:
            calcular_total(pedidos)

    elif opcion == "4":
        pedidos.clear()
        print("Pedido cancelado")

    elif opcion == "5":
        print("Gracias por usar la app")
        break

    else:
        print("Opción inválida") 

