from TDA_Lista import Lista
# el visual me da un error AttributeError: 'str' object has no attribute 'hora' que no se como se soluciona

list = Lista


personajes = ['Scalet Witch', 'Thor', 'Loki','Iron Man']

otraLista = ['Loki', 'Black Widow', 'Hulk', 'Rocket Racoonn']

for pers in personajes:
    list.insertar(pers)


pos = list.busqueda("Thor") # A
if (pos!= -1):
    print ("Thor esta en la lista, en la posicion ",+pos)
else:
    print("Thor no esta en la lista!")


pos = list.busqueda("Scalet Witch") # B
list.modificar_elemento(pos,"Scarlet Witch")


for pers in personajes: # C
    list.insertar(pers)


list.barrido() #D
list.barrido_descendente()


print (list.obtener_elemento(7)) #E


for i in range (0, list.tamanio()-1): # F
    personaje = list.obtener_elemento(i)
    if (personaje[0:1] == "C") or (personaje[0:1] == "S"): 
        print (personaje)

personajess = (personajes+otraLista)
list.barrido_eliminando(personajess)

# G
SuperH = [
    {'name':'Scarlet Witch','anio':1939,'heroe':True},
    {'name':'Thor','anio':1963,'heroe':True},
    {'name':'Loki','anio':1962,'heroe':False},
    {'name':'Iron Man','anio':1963,'heroe':True},
    {'name':'Rocket Racconn', 'anio':1963, 'heroe':True},
    {'name':'Hulk', 'anio':1963, 'heroe':True},
    {'name':'Black Widow', 'anio':1963, 'heroe':True},
]

for pers in SuperH:
    list.insertar(pers,'name')

list.barrido()
list.ordenar('anio')
list.barrido()
