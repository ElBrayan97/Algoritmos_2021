def barrido(a):
    if(len(a)>0):
        print(a[0])
        barrido(a[1:])

def busqueda(a):
    if(len(a)>0):
        if a[0] == "yoda":
            print("yoda esta en la lista")
        else:
            busqueda(a[1:])

lista = ["p1","p2","yoda","p3"]

barrido(lista)
busqueda(lista)