from TDA_Cola import Cola
from TDA_Pila import pila

notificaciones = Cola()
insta = pila()

def eliminar_facebook(notificaciones): # A
    for i in range(0, notificaciones.tamanio()-1):
        aux = notificaciones.atencion()
        if (aux[1] ==  "Facebook"):
            aux = None
        else: 
            notificaciones.move_end()
        

def mostrar_twitter(notificaciones): # B
    for i in range (0, notificaciones.tamanio()-1):
        if (notificaciones.en_frente()[1] == "Twitter") and (notificaciones.en_frente()[2] == "Python") :
            aux = notificaciones.atencion()
            print(aux)
            notificaciones.arribo(aux)
        else:
            notificaciones.move_end()

def instagram(notificaciones, insta): # C
    for i in range (0, notificaciones.tamanio()-1):
        if (notificaciones.en_frente()[1] == "Instagram"):
            insta.apilar(notificaciones.atencion())
            
    while not insta.pila_vacia():
        print(insta.desapilar())




notificaciones.arribo([16, "Instagram", "mensaje"])
notificaciones.arribo([17, "Instagram", "mensaje"])
notificaciones.arribo([18, "Twitter", "Python" ])
notificaciones.arribo([19, "Twitter", "mensaje" ])
notificaciones.arribo([19, "Twitter", "Python" ])
notificaciones.arribo([20, "Facebook", "hola" ])
notificaciones.arribo([21, "Facebook", "hola" ])

eliminar_facebook(notificaciones)
mostrar_twitter(notificaciones)
instagram(notificaciones, insta)