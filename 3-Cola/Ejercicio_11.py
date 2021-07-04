from TDA_Cola import Cola

################# HELPER FUNCTIONS #################
def cargar_personajes(DS):
    DS.arribo(["Han Solo","Corellia"])
    DS.arribo(["Luke Skywalker","Tierra"])
    DS.arribo(["Yoda","Planeta1"])
    DS.arribo(["Personaje1","Alderaan"])
    DS.arribo(["Personaje2","Endor"])
    DS.arribo(["Jar Jar Binks","Planeta4"])
    DS.arribo(["Personaje3","Tatooine"])
    DS.arribo(["Personaje4","J"])

def barrido_cola(DS):
    for i in range (0, DS.tamanio()):
        print(DS.move_end()[0])

################# HELPER FUNCTIONS #################

def mostrar_AET(P):
    print("PLANETAS A-E-T")
    for i in range(0,P.tamanio()):
        A = P.atencion()
        if A[1]=="Alderaan" or A[1]=="Endor" or A[1]== "Tatooine":
            print (A[0])
            P.arribo(A)
        else:
            P.arribo(A)

def planeta_natal(P):
    print ("PLANETA NATAL")
    for i in range(0, P.tamanio()-1):
        if (P.en_frente()[0]=="Han Solo") or (P.en_frente()[0]=="Luke Skywalker"):
            A = P.move_end()
            print (A[1])
        else:
            P.move_end()

def insertar(P):
    print("INSERTAR")
    for i in range(0, P.tamanio()-1):
        if (P.en_frente()[0]=="Yoda"):
            P.arribo(["Personaje8","Unplanetarandom"])
            P.move_end()
        else:
            P.move_end()

def eliminar(P):
    print("ELIMINAR")
    for i in range(0, P.tamanio()-1):   
        if (P.en_frente()[0] == "Jar Jar Binks"):
            P.move_end()
            print ("Se removio a: ", P.atencion()[0])
        else:
            P.move_end()



Personajes = Cola()
# Nombre = 0 y Planeta = 1
cargar_personajes(Personajes)
##
mostrar_AET(Personajes)
print("")
planeta_natal(Personajes)
print("")
insertar(Personajes)
print("")
eliminar(Personajes)
print("")

##
print("BARRIDO")
barrido_cola(Personajes)