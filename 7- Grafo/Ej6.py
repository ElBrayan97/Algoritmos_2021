from TDA_Grafo import Grafo
'''Partiendo del árbol genealógico de los dioses griegos que se observa en la imagen del ejercicio
20 de la guía de árboles (capítulo X), convertirlo en un grafo y resolver las siguientes actividades:
A. además del nombre de los dioses, deberá cargar una breve descripción de quien es o lo que
representa, no más de 20 palabras;
b. deberá cargar todas las relaciones entre los distintos dioses: padre, madre, hijo, hermano,
pareja, la etiquetas de dichas aristas son estos nombre de relación.
C. dado el nombre de un dios mostrar los hijos de este;
D. dado el nombre de un dios mostrar su nombre, padre, madre, hermanos y sus hijos;
E. determinar si existe relación directa entre dos vértice cualquieras, de ser así cual es la relación
entre ambos;
F. dados dos dioses determinar el camino más corto entre estos y mostrarlo. Considere como
camino más corto el que tenga menor número de aristas;
F. realizar un barrido en profundidad y amplitud de dicho grafo;
H. realizar un barrido mostrando el nombre de cada dios y el de su madre;
I. mostrar todos los ancestros de un determinado dios;
J. mostrar todos los nietos de Cronos;
K. mostrar todos los hijos de Tea;
L. persista los datos del grafo en archivos, uno para los vértices y otro para las aristas.'''

DiosesGriegos = Grafo()

file = open('Dioses.txt', encoding="utf8")
lineas = file.readlines()
lineas.pop(0)
for linea in lineas:
    dios = linea.split(';')
    dios_data = {}
    nombre = dios[0]
    dios_data['descripcion'] = dios[5]
    dios_data['genero'] = dios[6]
    DiosesGriegos.insertar_vertice(nombre, data = dios_data)

for linea in lineas:
    dios = linea.split(';')
    nombre = dios[0]
    padre = dios[1]
    madre = dios[2]
    hermanos = dios[3].split('/')#Devuelve solo un array en lugar de una linea de texto
    hijos = dios[4].split('/')
    genero = dios[6]
    pareja = dios[7].split('\n')[0]
    if (madre != '-'):
        DiosesGriegos.insertar_arista(1, nombre, madre, data = 'hijo/a')
    if (padre != '-'):
        DiosesGriegos.insertar_arista(1, nombre, padre, data = 'hijo/a')
    if (hijos[0] != '-'): # porque se creo una lista con un unico elemento que es '-' si no tiene hijos
        for hijo in hijos:
            if (genero == 'F'):
                DiosesGriegos.insertar_arista(1, nombre, hijo,  data = 'madre')
            else:
                DiosesGriegos.insertar_arista(1, nombre, hijo,  data = 'padre')
    if (hermanos[0] != '-'): # porque se creo una lista con un unico elemento que es '-' si no tiene hermanos
        for hermano in hermanos: 
            DiosesGriegos.insertar_arista(1, nombre, hermano, data = 'hermano/a')
    
    if (pareja != '-'):
        DiosesGriegos.insertar_arista(1, nombre, pareja, data = 'pareja')

print('Ejercicio 06')
print()

#! ---- PUNTO C ----!#
# c. dado el nombre de un dios mostrar los hijos de este;
nombre_dios = input('Ingrese el nombre de un dios para ver a sus hijos: ').capitalize()
hijos = DiosesGriegos.hijos_dios(nombre_dios)
if (hijos == None):
    print ('El dios ingresado no se encuentra cargado.')
elif (not hijos == []):
    print ('Los hijos de', nombre_dios, 'son:')
    for hijo in hijos:
        print (' - ', hijo)
else:
    print ('No hay informacion sobre los hijos de', nombre_dios)
print()

#! ---- PUNTO D ----!#
# d. dado el nombre de un dios mostrar su nombre, padre, madre, hermanos y sus hijos;
nombre_dios = input('Ingrese el nombre de un dios para ver a su familia: ').capitalize()
padres, hijos, hermanos = DiosesGriegos.familia_dios(nombre_dios)

if (padres == None):
    print ('El dios ingresado no se encuentra cargado.')
else:
    print ('Miembros de la familia de', nombre_dios, ':')    
    if (not padres == []):
        print ('Padres:')
        for padre in padres:
            print (' -', padre)
    if (not hermanos == []):            
        print ('Hermanos:')
        for hermano in hermanos:
            print (' -', hermano)
    if (not hijos == []):            
        print ('Hijos:')
        for hijo in hijos:
            print (' -', hijo)    
print()


#! ---- PUNTO E ----!#
# e. determinar si existe relación directa entre dos vértice cualquieras, de ser así cual es la relación
# entre ambos;
print('A continuacion, ingrese los nombres de dos DiosesGriegos para determinar si tienen una relacion directa.')
vertice_origen = input('Ingrese el nombre del primer dios: ').capitalize()
vertice_destino = input('Ingrese el nombre del segundo dios: ').capitalize()
relaciones = DiosesGriegos.relacion_dioses(vertice_origen, vertice_destino)
if (not relaciones == []):
    print ('Relacion(es) entre', vertice_origen, 'y', vertice_destino, ':')
    for relacion in relaciones:
        print(' - ', vertice_origen, 'es', relacion, 'de', vertice_destino)
else:
    print('No existe relacion directa entre', vertice_origen, 'y', vertice_destino)
print()

#! ---- PUNTO F ----!#
# f. dados dos DiosesGriegos determinar el camino más corto entre estos y mostrarlo. Considere como
# camino más corto el que tenga menor número de aristas;

print('A continuacion, ingrese los nombres de dos DiosesGriegos para determinar el camino mas corto entre ambos.')
dios1 = input('Ingrese el nombre del primer dios: ').capitalize()
dios2 = input('Ingrese el nombre del segundo dios: ').capitalize()
print()
ver_origen = DiosesGriegos.buscar_vertice(dios2)
ver_destino = DiosesGriegos.buscar_vertice(dios1)

pila_camino = DiosesGriegos.dijkstra(ver_origen, ver_destino)

destino = dios1
costo = None

print ('El camino mas corto es:')
while(not pila_camino.pila_vacia()):
    dato = pila_camino.desapilar()
    if(dato[1][0] == destino):
        if(costo is None):
            costo = dato[0]
        print(' - ', dato[1][0])
        destino = dato[1][1]

print('El costo total del camino es', costo)
print()

#! ---- PUNTO G ----!#
# g. realizar un barrido en profundidad y amplitud de dicho grafo;
a = input('Presione enter para ver el barrido en profundidad.')
DiosesGriegos.barrido_profundidad(0)
print()
DiosesGriegos.marcar_no_visitado()
a = input('Presione enter para ver el barrido en amplitud.')
DiosesGriegos.barrido_amplitud(0)
DiosesGriegos.marcar_no_visitado()
print()

#! ---- PUNTO H ----!#
# h. realizar un barrido mostrando el nombre de cada dios y el de su madre;
a = input('Presione enter para ver el barrido de los DiosesGriegos y sus madres.')
DiosesGriegos.barrido_profundidad_dioses_madres(0)
DiosesGriegos.marcar_no_visitado()
print()

#! ---- PUNTO I ----!#
# i. mostrar todos los ancestros de un determinado dios;
ancestros = []
nombre_dios = input('Ingrese el nombre de un dios para ver a sus ancestros: ').capitalize()
DiosesGriegos.ancestros_dios(nombre_dios, ancestros)
if (not ancestros == []):
    print('Ancestros de', nombre_dios)
    for ancestro in ancestros:
        print(' - ', ancestro)
else:
    print ('No hay informacion sobre los ancestros de', nombre_dios)
print()

#! ---- PUNTO J ----!#
# j. mostrar todos los nietos de Cronos;
print ('Nietos de Cronos:')
nietos = DiosesGriegos.nietos_dios('Kronos')
for nieto in nietos:
    print (' - ', nieto)
print()

#! ---- PUNTO K ----!#
# k. mostrar todos los hijos de Tea;
print ('Los hijos de Tea son:')
hijos = DiosesGriegos.hijos_dios('Theia')
for hijo in hijos:
    print (' - ', hijo)
print()
