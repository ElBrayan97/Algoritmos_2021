from TDA_Cola import Cola

C=Cola()

def cargar_cola(C):
    C.arribo(["Steve Rogers","Capitán América","M"])
    C.arribo(["Tony Stark","Iron Man", "M"])
    C.arribo(["Natasha Romanoff","Black Widow","F"])
    C.arribo(["Carol Danvers", "Capitana Marvel", "F"])
    C.arribo(["Peter Parker", "Spyder-Man", "M"])
    C.arribo(["Scot Lang", "Ant-Man", "M"])
    C.arribo(["Stephen Strange", "Dr. Strange", "M"])
    C.arribo(["Wanda Maximof", "Bruja Escarlata", "F"])
    C.arribo(["Bruce Banner", "Hulk", "M"])
    C.arribo(["T'Challa", "Pantera Negra", "M"])
    print("Cola Cargada!")

def determinar(C): # A
    aux=Cola()
    while not C.cola_vacia():
        data = C.atencion()
        if (data[1]=="Capitana Marvel"):
            print ("Capitana Marvel es: ",data[0])
        aux.arribo(data)
        if data[2]=="F":
            print (data)
        else:
            print (data)
        if data[0]=="Scot Lang":
            print ("Scot Lang es: ", data[1])
    while not aux.cola_vacia():
        C.arribo(aux.atencion())


def feminismo4ever(C): # B
    aux=Cola()
    while not C.cola_vacia():
        data = C.atencion()
        if (data[1]=="Capitana Marvel"):
            print ("Capitana Marvel es: ",data[0])
        aux.arribo(data)
        if data[2]=="F":
            print (data)
        else:
            print (data)
        if data[0]=="Scot Lang":
            print ("Scot Lang es: ", data[1])
    while not aux.cola_vacia():
        C.arribo(aux.atencion())

def scotLang(C):
    aux=Cola()
    while not C.cola_vacia():
        data = C.atencion()
        if (data[1]=="Capitana Marvel"):
            print ("Capitana Marvel es: ",data[0])
        aux.arribo(data)
        if data[2]=="F":
            print (data)
        else:
            print (data)
        if data[0]=="Scot Lang":
            print ("Scot Lang es: ", data[1])
    while not aux.cola_vacia():
        C.arribo(aux.atencion())

