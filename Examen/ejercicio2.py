from TDA_Cola import Cola
from TDA_Pila import pila
"""
lo hice pensando en un sublista de cada una de las posiciones de la cola y la pila, y los 
datos tienen el orden del ejercicio, 0:Hora. 1:Aplicacion. 2:Mensaje.
"""
def eliminar_facebook(notificaciones):
    for i in range(0,len(notificaciones)):
        aux = notificaciones.atencion()
        if aux[1] == "Facebook":
            aux = []
        else:
            notificaciones.move_end()
        

def mostrar_twitter(notificaciones):
    for i in range (0,len(notificaciones)):
        if notificaciones.en_frente()=="Twitter":
            aux = notificaciones.atencion()
            print("Python: ",aux[2])
            notificaciones.arribo(aux)

def instagram(notificaciones, insta):
    while not notificaciones.cola_vacia:
        if notificaciones.en_frente()[1]=="Instagram":
            insta.apilar(notificaciones.atencion())

    while not insta.pila_vacia():
        print(insta.desapilar())
        



notificaciones = Cola
insta = pila

eliminar_facebook(notificaciones)
mostrar_twitter(notificaciones)
instagram(notificaciones, insta)