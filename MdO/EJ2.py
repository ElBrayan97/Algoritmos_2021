from TDA_Grafo import Grafo


'''Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos
necesarios para resolver las tareas, listadas a continuación:

1) Cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
2) Realizar un barrido en profundidad y amplitud partiendo desde las tres notebook: 
Red Hat, Debian, Arch;
3) Encontrar el camino más corto para enviar a imprimir un documento desde la pc:
Debian y Red Hat, hasta el servidor “MongoDB”;
4) Encontrar el árbol de expansión mínima;
5) La impresora esta temporalmente fuera de linea por mantenimiento, quítela del grafo y
realice un barrido en profundidad para corroborar que efectivamente fue borrada;
6) Debe utilizar un grafo no dirigido'''

#Debemos indicar mediante la variable booleana dirigido, si el grafo 
#es dirigido tendrá valor verdadero y si es no dirigido falso
network=Grafo(dirigido=False)

#1)Cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
network.insertar_vertice('Manjaro', data = {'PC'})
network.insertar_vertice('Parrot', data = {'PC'})
network.insertar_vertice('Fedora', data = {'PC'})
network.insertar_vertice('Mint', data = {'PC'})
network.insertar_vertice('Ubuntu', data = {'PC'})
network.insertar_vertice('Arch', data = {'Notebook'})
network.insertar_vertice('Debian', data = {'Notebook'})
network.insertar_vertice('Red Hat', data = {'Notebook'})
network.insertar_vertice('Router 1', data = {'Router'})
network.insertar_vertice('Router 2', data = {'Router'})
network.insertar_vertice('Router 3', data = {'Router'})
network.insertar_vertice('Guarani', data = {'Servidor'})
network.insertar_vertice('MongoDB', data = {'Servidor'})
network.insertar_vertice('Switch 1', data = {'Switch'})
network.insertar_vertice('Switch 2', data = {'Switch'})   
network.insertar_vertice('Impresora', data = {'impresora'})

network.insertar_arista(40, 'Manjaro', 'Switch 2')
network.insertar_arista(12, 'Parrot',   'Switch 2')
network.insertar_arista(5,  'MongoDB',  'Switch 2')
network.insertar_arista(56, 'Arch',     'Switch 2')
network.insertar_arista(40, 'Manjaro',  'Switch 2')
network.insertar_arista(61, 'Router 3', 'Switch 2')
network.insertar_arista(43, 'Router 1', 'Router 3')
network.insertar_arista(50, 'Router 2', 'Router 3')
network.insertar_arista(37, 'Router 2', 'Router 1')
network.insertar_arista(9,  'Router 2', 'Guarani')
network.insertar_arista(25, 'Router 2', 'network Hat')
network.insertar_arista(29, 'Router 1', 'Switch 1')
network.insertar_arista(17, 'Switch 1', 'Debian')
network.insertar_arista(18, 'Switch 1', 'Ubuntu')
network.insertar_arista(22, 'Switch 1', 'Impresora')
network.insertar_arista(80, 'Switch 1', 'Mint')

#2)Realizar un barrido en profundidad y amplitud partiendo desde las tres notebook:
# Red Hat, Debian, Arch;

pos = network.buscar_vertice('Red Hat') 
print('Barrido en profundidad de Red Hat Es:')
network.barrido_profundidad(pos)
network.marcar_no_visitado()
print('')
print('Barrido en Amplitud de Red Hat:')
network.barrido_amplitud(pos)
network.marcar_no_visitado()
print('')

pos = network.buscar_vertice('Debian') 
print('El Barrido En Profundidad De Debian Es:')
network.barrido_profundidad(pos)
network.marcar_no_visitado()
print('')
print('El Barrido En Amplitud De Debian Es:')
network.barrido_amplitud(pos)
network.marcar_no_visitado()
print('')

pos = network.buscar_vertice('Arch')
print('El Barrido En Profundidad De Es Arch:')
network.barrido_profundidad(pos)
network.marcar_no_visitado()
print('')
print('El Barrido En Amplitud De Arch Es:')
network.barrido_amplitud(pos)
network.marcar_no_visitado()
print('')

########################################################################################

#3) Encontrar el camino más corto para enviar a imprimir un documento desde la pc:
#Debian y Red Hat, hasta el servidor “MongoDB”;

def camino_mas_corto(network):
    camino = network.dijkstra(network.buscar_vertice('Red Hat'),network.buscar_vertice('MongoDB'))
    print(" El Camino Mas Corta De Red Hat a MongoDB Es:")
    while not camino.pila_vacia():
        print(camino.desapilar())

    camino = network.dijkstra(network.buscar_vertice('Debian'),network.buscar_vertice('MongoDB'))
    print(" El Camino Mas Cort De Debian a MongoDB Es:")
    while not camino.pila_vacia():
        print(camino.desapilar())

    print("Ruta mas corta MongoDB - Impresora")
    camino = network.dijkstra(network.buscar_vertice('MongoDB'),network.buscar_vertice('Impresora'))
    while not camino.pila_vacia():
        print(camino.desapilar())




#4) Encontrar el árbol de expansión mínima;

def arbol_minimo(network):
    pass

#5) La impresora esta temporalmente fuera de linea por mantenimiento, quítela del grafo y
#realice un barrido en profundidad para corroborar que efectivamente fue borrada;

def eliminar_impresora(network):
    print ('Elimino La Impresora: ')
    network.eliminar_vertice('Impresora')
    print ('El Barrido En Profundidad Es:')
    network.barrido_profundidad(network.buscar_vertice('Red Hat'))


#cargar_aristas(network)

#barridos(network)

#rutamascorta(network)

#arbol_minimo(network)

print('El Arbol De Expansion Minima Es:')
bosque = network.prim()
for item in bosque:
    print (item[1])

eliminar_impresora(network)
