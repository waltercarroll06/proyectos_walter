usuarios = {
    "walter": {
        "telefono": "3001110000",
        "password": "1234",
        "saldo": 1000
    },
    "sofia": {
        "telefono": "3002220000",
        "password": "abcd",
        "saldo": 1500
    },
    "carlos": {
        "telefono": "3003330000",
        "password": "5678",
        "saldo": 2000
    },
    "laura": {
        "telefono": "3004440000",
        "password": "pass",
        "saldo": 2500
    },
    "andres": {
        "telefono": "3005550000",
        "password": "0000",
        "saldo": 3000
    }
}

intentos = 3
def log_in(usuarios , usuario , contraseña):
    if usuario not in usuarios:
        raise ValueError("error: usuario no encontrado")
    if usuarios[usuario]["password"] != contraseña:
        raise ValueError("error: contraseña incorrecta")
    return usuario


intentos = 3
while intentos > 0:
    try:
        usuario = input("ingresa tu nombre de usuario: ")
        contraseña = input("ingresa tu contraseña: ")
        usuario_valido = log_in(usuarios , usuario , contraseña)
        print("Bienvenido", usuario_valido)
        break
    except ValueError as e:
        print(e)
        intentos -= 1
        print("intentos: " , intentos)
if intentos == 0:
    print("cuenta bloqueda")
    exit()

0


def depositar_dinero(saldo , deposito):
    if deposito <= 0:
        raise ValueError("error: deposito no valido")
    if deposito > 10000:
        raise ValueError("error: monto del deposito mayor a 10 mil")
    return  saldo + deposito
    
def retira_dinero(saldo , retiro):
    if retiro > saldo:
        raise ValueError("retiro no permitido excede el valor del saldo")
    if retiro <= 0:
        raise ValueError("error: retiro de dinero no valido")
    return saldo - retiro
    



opcion_usuario = ""
while opcion_usuario != "4":
    print("\n====================")
    print("     BANCO APP")
    print("====================")
    print("1) Depositar dinero")
    print("2) Retirar dinero")
    print("3) Ver saldo")
    print("4) Salir")
    print("====================")
    

    opcion_usuario = input("ingresa una opcion: ")

    if opcion_usuario == "1":
        try:
            deposito_usuario= int(input(f"Hola {usuario}, ¿cuánto deseas depositar?: "))
            print(f"tu deposito fue de: {deposito_usuario}")
    
            deposito = depositar_dinero(usuarios[usuario]["saldo"] , deposito_usuario)
        
            usuarios[usuario]["saldo"] = deposito
            print("tu saldo total es de: " ,  usuarios[usuario]["saldo"])
        
        except ValueError as e:
            print(e)
    
    elif opcion_usuario == "2":
        confirmacion = True
        while confirmacion:
            try:
                retiro_usuario = int(input(f"Hola {usuario}, ¿cuánto deseas retirar?: "))
                opcion = input((f"deseas retirar: {retiro_usuario} ?: ")).lower()
                if opcion == "si":
                    confirmacion = False
                elif opcion == "no":
                    print("operacion cancelada")
                    break
                else:
                    print("opcion invalida(si/no)")
            except ValueError as e:
                print(e)
        
        if not confirmacion:
            saldo_restante = retira_dinero(usuarios[usuario]["saldo"], retiro_usuario)
            usuarios[usuario]["saldo"] = saldo_restante
            print(f"retiro existoso, saldo restante: {usuarios[usuario]["saldo"]}")
    
    elif opcion_usuario == "3":
            print(f"{usuario} tu saldo es de {usuarios[usuario]["saldo"]}")
    

    elif opcion_usuario == "4":
        break
    else:
        print("opcion no valida intente de nuevo")

