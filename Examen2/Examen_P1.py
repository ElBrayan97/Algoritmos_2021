from TDA_Arboles import Arbol

datos = [ #9
    {'nombre':"Dino 0", 'code': 73530, 'zona':"7A"},
    {'nombre':"Dino 1", 'code': 12300, 'zona':"7B"},
    {'nombre':"Raptor", 'code': 792, 'zona':"8C"},
    {'nombre':"Raptor", 'code': 44440, 'zona':"9A"},
    {'nombre':"Dino 4", 'code': 24574, 'zona':"3Z"},
    {'nombre':"T-Rex", 'code': 94385, 'zona':"A1"},
    {'nombre':"T-Rex", 'code': 78934, 'zona':"J3"},
    {'nombre':"Dino 7", 'code': 67894, 'zona':"M1"},
    {'nombre':"Sgimoloch", 'code': 89238, 'zona':"M2"},
    {'nombre':"Dino 9", 'code': 12345, 'zona':"D4"},
    {'nombre':"Dino 8", 'code': 54244, 'zona':"C4"},
    {'nombre':"Diplodocus", 'code': 67114, 'zona':"M6"},
    {'nombre':"Sgimoloch", 'code': 89118, 'zona':"M2"},
    {'nombre':"Dino 9", 'code': 12115, 'zona':"D4"},
    {'nombre':"Dino 8", 'code': 54114, 'zona':"C4"}
]

Arbol_Nombres = Arbol()
Arbol_Code = Arbol()

#1 Y 2
for dino in datos: #Carga
    Arbol_Nombres =  Arbol_Nombres.insertar_nodo(dino['nombre'], dino)
    Arbol_Code = Arbol_Code.insertar_nodo(dino['code'],dino)

#3
print ("\nBarrido por nombre")
Arbol_Nombres.inorden()

#4
print("\nDino codigo 792:")
nodo = Arbol_Code.busqueda(792)
print ("Nombre: ",nodo.datos['nombre'])
print ("Zona Asignada: ",nodo.datos['zona'])


#5
print ("\nT-Rex en la isla: ")
Arbol_Nombres.inorden_REX("T-Rex")


#6
#info,datos = Arbol_Nombres.busqueda("Sgimoloch")
#print (info, datos)
#Arbol_Nombres.eliminar_nodo(info)
#Arbol_Code.busqueda

#Arbol_Nombres.inorden()

#7
print ("\nUbicacion de los Raptores en la isla: ")
Arbol_Nombres.inorden_raptor("Raptor")


#8    
name = "Diplodocus"
print ("\nEn la isla hay :",Arbol_Nombres.contar_dinos(name), name)