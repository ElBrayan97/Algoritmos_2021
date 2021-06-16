from TDA_Lista import Lista

list = Lista
aux_list = Lista

def esta_thor(list):
    pos = (list.busqueda("Thor"))
    if (pos != -1):
        print("Thor esta en la lista en la posicion: ", pos)
    else:
        print("Thor no esta en la lista")

def cambiar_nombre(list):
    pos = list.busqueda("Scalet Witch")
    if (pos != -1):
        list.modificar_elemento(pos,"Scarlet Witch")

def añadir(list, aux_list):
    for i in (1,len(aux_list)-1):
        aux = aux_list.obtener_elemento(i)
        pos = list.buscar(aux)
        if pos != -1:
            print(aux," ya esta en la lista")
        else:
            list.insertar(aux)

def barridos(list):
    for i in range (0, list.tamanio()): #ascendente
        print(list.obtener_elemento(i))

    for i in range (list.tamanio(), 0): #descendente
        print(list.obtener_elemento(i))



def CoS(list):
    for i in range(0, list.tamanio()):
        aux = list.obtener_elemento(i)
        if aux[0:1]=="C" or aux[0:1]=="S":
            print (aux)
            
            

esta_thor(list)
cambiar_nombre(list)
añadir(list,aux_list)
barridos(list)
print (list.obetener_elemento(7))
CoS(list)
