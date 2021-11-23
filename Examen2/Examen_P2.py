from TDA_Grafo import Grafo

red = Grafo(dirigido=False)

datos_nodos = [{'name': 'Red Hat', 'tipo' : 'notebook'},
                {'name': 'Debian', 'tipo' : 'notebook'},
                {'name': 'Ubuntu', 'tipo' : 'pc'},
                {'name': 'Impresora', 'tipo' : 'impresora'},
                {'name': 'Mint', 'tipo' : 'pc'},
                {'name': 'Switch 1', 'tipo' : 'switch'},
                {'name': 'Router 1', 'tipo' : 'router'},
                {'name': 'Router 2', 'tipo' : 'router'},
                {'name': 'Router 3', 'tipo' : 'router'},
                {'name': 'Guarani', 'tipo' : 'servidor'},
                {'name': 'Manjaro', 'tipo' : 'pc'},
                {'name': 'Switch 2', 'tipo' : 'switch'},
                {'name': 'Fedora', 'tipo' : 'pc'},
                {'name': 'Arch', 'tipo' : 'notebook'},
                {'name': 'MongoDB', 'tipo' : 'servidor'},
                {'name': 'Parrot', 'tipo' : 'pc'}
]

for nodo in datos_nodos:
    red.insertar_vertice(nodo['name'],data=nodo['tipo'])

def cargar_aristas (red):#Conexiones entre los nodos
    red.insertar_arista(25, 'Red Hat', 'Router 2')
    red.insertar_arista(17, 'Debian', 'Switch 1')
    red.insertar_arista(18, 'Ubuntu', 'Switch 1')
    red.insertar_arista(22, 'Impresora', 'Switch 1')
    red.insertar_arista(80, 'Mint', 'Switch 1')
    red.insertar_arista(29, 'Switch 1', 'Router 1')
    red.insertar_arista(37, 'Router 1', 'Router 2')
    red.insertar_arista(43, 'Router 1', 'Router 3')
    red.insertar_arista(50, 'Router 2', 'Router 3')
    red.insertar_arista(9, 'Guarani', 'Router 2')
    red.insertar_arista(61, 'Router 3', 'Switch 2')
    red.insertar_arista(40, 'Switch 2', 'Manjaro')
    red.insertar_arista(12, 'Switch 2', 'Parrot')
    red.insertar_arista(5, 'Switch 2', 'MongoDB')
    red.insertar_arista(3, 'Switch 2', 'Fedora')
    red.insertar_arista(56, 'Switch 2', 'Arch')


#2
def barridos(red):
    print ('\nINICIO BARRIDO EN AMPLITUD:')
    print ("\nBarrido Red Hat:")
    red.barrido_amplitud(red.buscar_vertice('Red Hat'))
    red.marcar_no_visitado()
    print ("\nBarrido Debian:")
    red.barrido_amplitud(red.buscar_vertice('Debian'))
    red.marcar_no_visitado()
    print ("\nBarrido Arch:")
    red.barrido_amplitud(red.buscar_vertice('Arch'))
    red.marcar_no_visitado()
    print ('\nINICIO BARRIDO EN PROFUNDIDAD:')
    print ("\nBarrido Red Hat:")
    red.barrido_profundidad(red.buscar_vertice('Red Hat'))
    red.marcar_no_visitado()
    print ("\nBarrido Debian:")
    red.barrido_profundidad(red.buscar_vertice('Debian'))
    red.marcar_no_visitado()
    print ("\nBarrido Arch:")
    red.barrido_profundidad(red.buscar_vertice('Arch'))
    red.marcar_no_visitado()
    print ('FIN BARRIDOS:')


def rutamascorta(red):
    ruta = red.dijkstra(red.buscar_vertice('Red Hat'),red.buscar_vertice('MongoDB'))
    print("\n\Ruta mas corta Red Hat - MongoDB")
    while not ruta.pila_vacia():
        print(ruta.desapilar())

    ruta = red.dijkstra(red.buscar_vertice('Debian'),red.buscar_vertice('MongoDB'))
    print("\Ruta mas corta Debian - MongoDB")
    while not ruta.pila_vacia():
        print(ruta.desapilar())

    print("\nRuta mas corta MongoDB - Impresora")
    ruta = red.dijkstra(red.buscar_vertice('MongoDB'),red.buscar_vertice('Impresora'))
    while not ruta.pila_vacia():
        print(ruta.desapilar())


def arbol_minimo(red):
    print('\nArbol de expansion minima:')
    bosque = red.prim()
    for item in bosque:
        print (item[1])

def eliminar_impresora(red):
    print ('\nELIMINANDO LA IMPRESORA: ')
    red.eliminar_vertice('Impresora')
    print ('BARRIDO:')
    red.barrido_profundidad(red.buscar_vertice('Red Hat'))

cargar_aristas(red)

barridos(red)

rutamascorta(red)

arbol_minimo(red)

eliminar_impresora(red)




