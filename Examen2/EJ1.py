from  TDA_ArbolBin import Arbol

"""El encargado de Jurassic World nos solicita que desarrollemos un algoritmo que nos permita
resolver los siguientes requerimientos:

1) Almacenar los datos de los distintos dinosaurios que hay en la isla, de cada uno se
conoce su nombre, código de cinco dígitos y zona de ubicación (un dígito y un carácter
por ejemplo 7A), existen varios dinosaurios con el mismo nombre pero sus códigos son
distintos, los códigos no pueden ser repetidos (tenga cuidado);
2) Se deben almacenar los datos en dos arboles uno ordenado por nombre y otro por código;
3) Realizar un barrido en orden del árbol ordenado por nombre;
4) Mostrar toda la información del dinosaurio 792;
5) Mostrar toda la información de todos los T-Rex que hay en la isla;
6) Modificar el nombre del dinosaurio en Sgimoloch en ambos arboles porque esta mal cargado, su nombre correcto es Stygimoloch;
7) Mostrar la ubicación de todos los Raptores que hay en la isla;
8) Contar cuantos Diplodocus hay en el parque;
9) Debe cargar al menos 15 elementos."""

#Nº1 cargo la lista que es dinamica para acceder a los datos.
Dinodatos=[{'nombre':'Parasaurolofus','codigo':'792','ubicacion':'7a'},
    {'nombre':'Saltasaurus','codigo':'78','ubicacion':'9i'},
    {'nombre':'Chirostenote','codigo':'67','ubicacion':'2s'},
    {'nombre':'Acronthosaurus','codigo':'89','ubicacion':'d3'},
    {'nombre':'Velociraptor','codigo':'10','ubicacion':'0a'},
    {'nombre':'Dilophosaurus','codigo':'67','ubicacion':'9t'},
    {'nombre':'Coelophysis','codigo':'01','ubicacion':'8g'},
    {'nombre':'Ceratosaurus','codigo':'02','ubicacion':'5g'},
    {'nombre':'Monolophosaurus','codigo':'11','ubicacion':'4g'},
    {'nombre':'Spinosaurus','codigo':'12','ubicacion':'3f'},
    {'nombre':'Astralopitecus','codigo':'13','ubicacion':'3g'},
    {'nombre':'Compsognathus','codigo':'15','ubicacion':'6i'},
    {'nombre':'Tyranosaurus Rex','codigo':'09','ubicacion':'2c'},
    {'nombre':'Tyranosaurus Rex','codigo':'10','ubicacion':'2b'},
    {'nombre':'Braquiosaurio','codigo':'03','ubicacion':'3x'},
    {'nombre':'Protoceratops.','codigo':'00','ubicacion':'5h'},
    {'nombre':'Sgimiloch','codigo':'23','ubicacion':'7x'}
]

#Punto 2
ArbolNombresDinos = Arbol()
ArbolCodigosDino = Arbol()
for Dino in Dinodatos:#Para cada Dinosaurio en el diccionario inserto los nodos. 
   ArbolNombresDinos = ArbolNombresDinos.insertar_nodo(Dino['nombre'],Dino) # por el arbol avl
   ArbolCodigosDino= ArbolCodigosDino.insertar_nodo(Dino['codigo'],Dino) # por el arbol avl
print()

#3)Realizar un barrido en orden del árbol ordenado por nombre;
print('PUNTO 3 / Barrido En Orden De Todo El Arbol Por Nombre:')
ArbolNombresDinos.inorden()
print('')

#4)Mostrar toda la información del dinosaurio 792;
print('PUNTO 4 / La Informacion Del Dinosaurio 792 Es:')
ArbolCodigosDino.mostrarDino_792('792')#devuelve el nodo del arbol
print()

#5)Mostrar toda la información de todos los T-Rex que hay en la isla;
print('PUNTO 5 / La Informacion De Todos Los T-Rex Es:')
ArbolNombresDinos.busqueda_Trex('Tyranosaurus Rex')
print('')

#6)Modificar el nombre del dinosaurio en Sgimoloch en ambos arboles porque esta mal
#cargado, su nombre correcto es Stygimoloch;
print('PUNTO 6 / Modificar Nombre Del Dinosaurio')
ArbolNombresDinos.modificar_dino()
print('')

#7)Mostrar la ubicación de todos los Raptores que hay en la isla;
print('Ubicacion de los Raptores')
ArbolNombresDinos.busqueda_Raptor('Raptor')
print('')



'''
#8 Contar cuantos Diplodocus hay en el parque;
print('Cantidad De Diplodocus:', ArbolNombresDinos.contar_ocurrencias('Diplodocus'))
'''