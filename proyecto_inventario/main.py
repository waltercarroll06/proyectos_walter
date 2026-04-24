from datetime import datetime


categorias = {
    "novelas": [
        "Harry Potter",
        "1984",
        "El principito",
        "Orgullo y prejuicio",
        "Cien años de soledad"
    ],
    "ciencia": [
        "Fisica basica",
        "Quimica general",
        "Biologia celular",
        "Astronomia para principiantes",
        "El gen egoista"
    ],
    "historia": [
        "Historia de Colombia",
        "Segunda guerra mundial",
        "La guerra fria",
        "Imperio romano",
        "Historia universal"
    ],
    "tecnologia": [
        "Python desde cero",
        "Algoritmos y estructuras de datos",
        "Inteligencia artificial",
        "Machine learning básico",
        "Ciberseguridad"
    ],
    "autoayuda": [
        "Habitos atomicos",
        "El poder del ahora",
        "Piense y hagase rico",
        "Como ganar amigos",
        "Los 7 habitos"
    ],
    "fantasia": [
        "El señor de los anillos",
        "Juego de tronos",
        "La rueda del tiempo",
        "Las cronicas de Narnia",
        "Eragon"
    ]
}


def rentar_libros(categorias):
    try:
        nombre = input("ingresa tu nombre: ")
        for index , categoria in enumerate(categorias , 1):
            print(f"{index}. {categoria}")
        
        opcion = int(input(f"\nhola {nombre} ingresa una categoria: "))
        if opcion > len(categorias) or opcion <= 0:
            raise ValueError ("numero invalido")
            
        lista_categorias = list(categorias.keys())
        categoria = lista_categorias[opcion - 1]

        for index , i in enumerate(categorias[categoria], 1):
            print(f"{index}. {i}")
        ocpion_libro = int(input("\nQue libro deseas rentar: "))
        libro_seleccionado = categorias[categoria][ocpion_libro -1]
        print(libro_seleccionado)


        fecha = datetime.now().strftime("%Y-%m-%d")

        with open("proyecto_inventario/data/inventario.txt", "a") as f:
            f.write(f"{nombre},{libro_seleccionado},{categoria},{fecha}\n")

    

    except ValueError as e:
        print(e)

while True:
    print("\n--- SISTEMA DE LIBROS ---")
    print("1. Rentar libro")
    print("2. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        rentar_libros(categorias)

    elif opcion == "2":
        print("Bye 👋")
        break

    else:
        print("Opción inválida ❌")
