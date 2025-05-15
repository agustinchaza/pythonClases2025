"""1 una funcion que me devuelva una palabra al azar

2 una funcion a la cual le paso una lista de letras y una palabra
devuelva la palabra reemplazando por guiones las letras que no estan en la lista

ejemplo ([a, e, i] , delfin) -> _e__i_


3 necesito una funcion que devuelva true si una letra esta en una palabra y false si la letra no esta

ejemplo ("a", delfin) ->false
        ("e", delfin) -> true
"""
import random

def plabra_al_azar():
    palabras=["bicicleta","estadio","hinchada","boleta","mate"]
    return random.choice(palabras)

def palabraEncriptada(listaEncontradas, palabra_a_descubrir):
    encriptada=""
    for letra in palabra_a_descubrir:
        if letra in listaEncontradas:
            encriptada=encriptada+letra
        else:
            encriptada+="_"
    return encriptada

def letra_en_palabra (letra,palabra):
    if letra in palabra: return True
    else: return False
    
    
palabra=plabra_al_azar()
vidas=3
listaEncontradas=[]
ganaste=False
while vidas>0 and not ganaste:
    letra=input("Ingrese una letra")
    
    if letra_en_palabra(letra=letra, palabra=palabra):
        listaEncontradas.append(letra)
        print(f"Bien, la letra {letra} esta en la palabra")
    else:
        vidas-=1
        print(f"Perdiste una vida, te quedan {vidas}")
        
    encriptada=palabraEncriptada(listaEncontradas=listaEncontradas, palabra_a_descubrir=palabra)
    print(encriptada)
    
    if not "_" in encriptada:
        ganaste=True
    


if ganaste:
    print("Felicitaciuones, ganaste")
else: print(f"Perdiste, te quedaste sin vidas, la palabra era {palabra}")
    
    

    
    
    
            
            

