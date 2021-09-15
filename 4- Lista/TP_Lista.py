from TDA_Lista import Lista

#Ejercicios para entregar 6, 7, 15 y 22 

SuperH = [
    {'name':'Batman','anio':1939,'casa_comic':'DC Comics','biografía':'traje'},
    {'name':'Iron Man','anio':1963,'casa_comic':'Marvel','biografía':'armadura'},
    {'name':'Spyder Man','anio':1962,'casa_comic':'Marvel','biografía':'traje'},
    {'name':'Dr. Strange','anio':1963,'casa_comic':'DC Comics','biografía':'capa'},
    {'name':'Linterna Verde','anio':1963,'casa_comic':'DC Comics','biografía':'traje'},
    {'name':'Wolverine','anio':1963,'casa_comic':'DC Comics','biografía':'ninguno'},
    {'name':'Capitana Marvel','anio':1963,'casa_comic':'Marvel','biografía':'traje'},
    {'name':'Mujer Maravilla','anio':1963,'casa_comic':'DC Comics','biografía':'traje'},
    {'name':'Flash','anio':1963,'casa_comic':'DC Comics','biografía':'traje'},
    {'name':'Star-Lord','anio':1963,'casa_comic':'Marvel','biografía':'ninguno'},
]

Lista_Super = Lista()

for SH in SuperH:
    Lista_Super.insertar(SH,'name')

Lista_Super.eliminar('Linterna Verde','name') # A

personaje = Lista_Super.obtener_elemento(Lista_Super.busqueda('Wolverine','name')) # B
print (personaje['anio'])

personaje = Lista_Super.obtener_elemento(Lista_Super.busqueda('Dr. Strange','name')) # C
personaje['casa_comic'] = 'Marvel'
Lista_Super.insertar(personaje,'name')

for i in range (0, Lista_Super.tamanio()-1): # D y E
    personaje = Lista_Super.obtener_elemento(i)
    if personaje['biografía'] == 'traje' or personaje['biografía'] == 'armadura':
        print (personaje['name']+ " usa un traje o una armadura")
    if personaje['anio'] < 1963:
        print (personaje['name']+ " aparecio antes de 1963")

personaje = Lista_Super.obtener_elemento(Lista_Super.busqueda('Capitana Marvel','name')) # F
print (personaje['name']+" pertenece a "+personaje['casa_comic'])
personaje = Lista_Super.obtener_elemento(Lista_Super.busqueda('Mujer Maravilla','name'))
print (personaje['name']+" pertenece a "+personaje['casa_comic'])

print (Lista_Super.obtener_elemento(Lista_Super.busqueda('Star-Lord','name'))) # G
print (Lista_Super.obtener_elemento(Lista_Super.busqueda('Flash','name')))

for i in range (0, Lista_Super.tamanio()-1): # H
    personaje = Lista_Super.obtener_elemento(i)
    if (personaje['name'][0:1] == "B") or (personaje['name'][0:1] == "M") or (personaje['name'][0:1] == "S"): 
        print (personaje['name'])

dc = 0
mv = 0

for i in range (0, Lista_Super.tamanio()-1): # I
    
    personaje = Lista_Super.obtener_elemento(i)
    if (personaje['casa_comic'] == "Marvel"):
        mv+=1
    else:
        dc+=1

print("Personajes de DC Comics: ",dc)
print("Personajes de Marvel Comics: ",mv)