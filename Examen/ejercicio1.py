lista = ["Darth Vader","Han Solo","Yoda","Luke Skywalker"]

def barrido(vector):
    if(len(vector)>0):
        print(vector[0])
        barrido(vector[1:])

def busqueda(vector):
    if(len(vector)>0):
        if vector[0] == "Yoda" or vector[0] == "yoda":
            print("Yoda se encuentra en el vector")
        else:
            busqueda(vector[1:])

barrido(lista)
busqueda(lista)