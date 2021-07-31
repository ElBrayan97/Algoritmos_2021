from TDA_Cola import Cola

C = Cola()

def cargar_cola(cola): # Carga de la cola
    cola.arribo(["Steve Rogers","Capitán América","M"])
    cola.arribo(["Tony Stark","Iron Man", "M"])
    cola.arribo(["Natasha Romanoff","Black Widow","F"])
    cola.arribo(["Carol Danvers", "Capitana Marvel", "F"])
    cola.arribo(["Peter Parker", "Spyder-Man", "M"])
    cola.arribo(["Scot Lang", "Ant-Man", "M"])
    cola.arribo(["Stephen Strange", "Dr. Strange", "M"])
    cola.arribo(["Wanda Maximof", "Bruja Escarlata", "F"])
    cola.arribo(["Bruce Banner", "Hulk", "M"])
    cola.arribo(["T'Challa", "Pantera Negra", "M"])
    print("Cola Cargada!")

def reconstruir(A,B):
    while not B.cola_vacia():
            A.arribo(B.atencion())


def determinar(cola): # A
    aux = Cola()
    while not cola.cola_vacia():
        data = cola.atencion()
        if (data[1]=="Capitana Marvel"):
            print ("Capitana Marvel es: ",data[0])
        aux.arribo(data)
    
    reconstruir(cola,aux)

def mujeres(cola): # B
    aux = Cola()
    print("Mujeres")
    while not cola.cola_vacia():
        data = cola.atencion()
        if data[2]=="F":
            print (data)
        aux.arribo(data)

    reconstruir(cola,aux)


def hombres(cola): #C
    aux = Cola()
    print ("Hombres: ")
    while not cola.cola_vacia():
        data = cola.atencion()
        if data[2]=="M":
            print (data)
        aux.arribo(data)
    
    reconstruir(cola,aux)

def scotLang(cola): #D
    aux = Cola()
    while not cola.cola_vacia():
        data = cola.atencion()
        if (data[0]=="Scot Lang"):
            print("Scot Lang es:", data[1])
        aux.arribo(data)

    reconstruir(cola,aux)

def conS(cola): #E
    print ("personajes con S:")
    aux = Cola()
    while not cola.cola_vacia():
        data = cola.atencion()
        if data[0][0:1]=="S":
            print (data)
        aux.arribo(data)

    reconstruir(cola,aux)

def carolDanvers(cola): #F
    aux = Cola()
    while not cola.cola_vacia():
        data = cola.atencion()
        if data[0] =="Carol Danvers":
            print ("Carol Danvers es: ",data[1])
        aux.arribo(data)

    reconstruir(cola,aux)

cargar_cola(C)
determinar(C)
mujeres(C)
hombres(C)
scotLang(C)
conS(C)
carolDanvers(C)