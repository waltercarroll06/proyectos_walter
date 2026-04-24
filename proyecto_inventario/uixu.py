import tkinter as tk
from datetime import datetime

categorias = {
    "novelas": [
        "Harry Potter","1984","El principito","Orgullo y prejuicio","Cien años de soledad"
    ],
    "ciencia": [
        "Fisica basica","Quimica general","Biologia celular","Astronomia para principiantes","El gen egoista"
    ],
    "historia": [
        "Historia de Colombia","Segunda guerra mundial","La guerra fria","Imperio romano","Historia universal"
    ],
    "tecnologia": [
        "Python desde cero","Algoritmos y estructuras de datos","Inteligencia artificial","Machine learning básico","Ciberseguridad"
    ],
    "autoayuda": [
        "Habitos atomicos","El poder del ahora","Piense y hagase rico","Como ganar amigos","Los 7 habitos"
    ],
    "fantasia": [
        "El señor de los anillos","Juego de tronos","La rueda del tiempo","Las cronicas de Narnia","Eragon"
    ]
}

def mostrar_libros():
    seleccion = lista_categorias.curselection()
    if not seleccion:
        return

    indice = seleccion[0]
    categoria = list(categorias.keys())[indice]

    lista_libros.delete(0, tk.END)

    for libro in categorias[categoria]:
        lista_libros.insert(tk.END, libro)

def rentar_libro():
    nombre = entry_nombre.get()

    seleccion_cat = lista_categorias.curselection()
    seleccion_lib = lista_libros.curselection()

    if not nombre or not seleccion_cat or not seleccion_lib:
        resultado.config(text="Completa todos los campos ❌")
        return

    categoria = list(categorias.keys())[seleccion_cat[0]]
    libro = categorias[categoria][seleccion_lib[0]]

    fecha = datetime.now().strftime("%Y-%m-%d")

    try:
        with open("data/inventario.txt", "a") as f:
            f.write(f"{nombre},{libro},{categoria},{fecha}\n")

        resultado.config(text=f"{nombre} rentó {libro} 📚")

    except:
        resultado.config(text="Error al guardar ❌")

# ventana
ventana = tk.Tk()
ventana.title("Sistema de Libros 📚")
ventana.geometry("400x420")

# nombre
tk.Label(ventana, text="Nombre").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

# categorías
tk.Label(ventana, text="Categorías").pack()
lista_categorias = tk.Listbox(ventana)
lista_categorias.pack()

for cat in categorias:
    lista_categorias.insert(tk.END, cat)

# botón ver libros
tk.Button(ventana, text="Ver libros", command=mostrar_libros).pack(pady=5)

# libros
tk.Label(ventana, text="Libros").pack()
lista_libros = tk.Listbox(ventana)
lista_libros.pack()

# botón rentar
tk.Button(ventana, text="Rentar libro", command=rentar_libro).pack(pady=10)

# resultado
resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()