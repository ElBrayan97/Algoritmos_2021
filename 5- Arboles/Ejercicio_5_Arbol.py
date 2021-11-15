from TDA_Arbol_Binario import Arbol

personajes=[{'name':"Spiderman",'afinidad':True},
            {'name':"Loki",'afinidad':False},
            {'name':"Iron Man",'afinidad':True},
            {'name':"CCCC",'afinidad':True},
            {'name':"Capitan America",'afinidad':True}
            ]




mcu = Arbol()

for personaje in personajes: #A
    mcu = mcu.insertar_nodo(personaje['name'],personaje)

#mcu.inorden() #B
#a = mcu.busqueda('C') # C sta cosas no c como hacerla


