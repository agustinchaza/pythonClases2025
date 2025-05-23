
historial = []
saldo = 1000


def calcularHistoriales ():
    global historial
    global saldo    
    depositos =[]
    extracciones = []
    for historia in historial:
        if historia["operacion"] == "Deposito":
            depositos.append(historia["monto"])
        elif historia["operacion"] == "Extraccion":
            extracciones.append(historia["monto"])
    return {"depositos": sum(depositos),
            "extracciones": sum(extracciones),
            "saldo":saldo}


def agregarHistorial (operacion, monto):
    global historial
    historial.append({"operacion": operacion, "monto": monto, "saldoFinal": saldo})
    return historial

def mostrarHistorial():
    if len(historial) == 0:
        print("No hay operaciones en el historial.")
    else:
        print("Historial de operaciones:")
        for operacion in historial:
            print(f"Operacion: {operacion['operacion']}, Monto: {operacion['monto']}, Saldo Final: {operacion['saldoFinal']}")


def mostrarSaldo():
    
    print(f"Tu saldo actual es: $ {saldo}")

mostrarSaldo()


def depositar():
    try:
        global saldo
        monto = float(input("Ingrese el monto a depositar: "))
        if monto > 0:
            saldo += monto
            print(f"Depósito exitoso. ")
            mostrarSaldo()
            agregarHistorial("Deposito", monto)
        else:
            print("Error: el monto debe ser mayor que cero.")
    except ValueError:
             print("Error: debe ingresar un número válido.")
    return saldo

def extraer():
    global saldo
    try:
        monto = float(input("Ingrese el monto a extraer: "))
        if monto > 0 and monto <= saldo:
            saldo -= monto
            print(f"Extraccion exitosa. Su nuevo saldo es: {saldo}")
            agregarHistorial("Extraccion", monto)
        elif monto > saldo:
            print("Fondos insuficientes.")
        else:
            print("El monto debe ser mayor que cero.")
    except ValueError:
        print("Debe ingresar un numero valido.")
    return saldo

seleccionOpciones = {
    "1": "saldo",
    "2": "depositar",
    "3": "extraer",
    "4": "historial",
    "5": "Salir"
}
def cajeroAutomatico (saldoInicial):
    global saldo
    global historial
    saldo = saldoInicial
    while True:
        print("Bienvenido.")
        for opcion, funcion in seleccionOpciones.items():
            print(f"{opcion}. {funcion}")  
        opcionElegida = input ("Selecciona una opcion: ")     
        if opcionElegida in seleccionOpciones:
            opcionEle = seleccionOpciones [opcionElegida]
            match opcionEle:
                case "saldo":
                    mostrarSaldo()
                case "depositar":
                    depositar()
                case "extraer":
                    extraer()
                case "historial":
                    mostrarHistorial()
                case "Salir":
                    salir = calcularHistoriales()
                    print(f"Total depositado: ${salir["depositos"]}")
                    print(f"Total extraido: ${salir["extracciones"]}")
                    print(f"Saldo final: ${salir["saldo"]}")
                    print("Gracias por usar el cajero automatico.")
                    break
        else:
            print("Opcion invalida, reintentalo. ")



cajeroAutomatico(1000)
    
