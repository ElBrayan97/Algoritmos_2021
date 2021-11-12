from TDA_Lista import Lista

entrenadores = Lista()
pokemones = Lista()

EntrenadorES = [
    {'name':"Entrenador A", 'torneosGanados':4, 'perdidas':2, 'ganadas':12, 'pokebals':[0,3,4,4]},
    {'name':"Entrenador B", 'torneosGanados':1, 'perdidas':5, 'ganadas':4, 'pokebals':[0,1,2,2,5]},
    {'name':"Entrenador C", 'torneosGanados':2, 'perdidas':3, 'ganadas':3, 'pokebals':[1,3,6]},
    {'name':"Entrenador D", 'torneosGanados':0, 'perdidas':0, 'ganadas':2, 'pokebals':[0,1,2,2,3,4,5]}
]

PokemonES = [
    {'name':'Charizard', 'level':17, 'tipo':'Fuego', 'subtype':'Volador'}, #1
    {'name':'Ninetales', 'level':40, 'tipo':'Fuego', 'subtype':'no posee'}, #5
    {'name':'Bulbasaur', 'level':24, 'tipo':'Planta', 'subtype':'Veneno'}, #0
    {'name':'Lucario', 'level':7, 'tipo':'Lucha', 'subtype':'Acero'}, #2
    {'name':'Mantine', 'level':2, 'tipo':'Agua', 'subtype':'Volador'}, #3
    {'name':'Mewtwo', 'level':36, 'tipo':'Psiquico', 'subtype':'no posee'}, #4
    {'name':'Terrakion', 'level':12, 'tipo':'Roca', 'subtype':'Lucha'}, #6
]


def armar_listas(EntrenadorES, PokemonES, L1, L2): 
    for entrenador in EntrenadorES:
        L1.insertar(entrenador,'name') # inserta un entrenador del json y lo ordena x nombre
    for pokemon in PokemonES:
        L2.insertar(pokemon,'name') # inserta un pokemon del json y lo ordena x nombre
    print ("\nEntrenadores:")
    L1.barrido()
    print ("\nPokemones:")
    L2.barrido()


def pokemonesEntrenador(L1): #A
    entrenador = input(str("\ningrese el nombre de un entrenador: "))
    entrenador = L1.obtener_elemento(L1.busqueda(entrenador,'name'))
    if entrenador != None:
        print ("El entrenador tiene ",len(entrenador['pokebals'])," pokemones")
    else:
        print ("El entrenador no existe")


def torneos_Ganados(L1): #B
    print ("\nEntrenadores con mas de 3 torneos ganados")
    for i in range(0, L1.tamanio()-1):
        entrenador = L1.obtener_elemento(i)
        if entrenador['torneosGanados']>3:
            print (entrenador['name'])


def pokemonConHacks(L1, L2): #C
    L1.reordenar('torneosGanados')
    entrenador = L1.obtener_elemento(L1.tamanio()-1)
    posPokemones = entrenador['pokebals']
    print('')
    subPokemon = Lista()
    for pokemon in posPokemones:
        subPokemon.insertar(L2.obtener_elemento(pokemon),'level')
    pokemon = subPokemon.obtener_elemento(subPokemon.tamanio()-1)
    print ("El pokemon con mas nivel es : ", pokemon['name'], "\nnivel: ",pokemon['level'],"\n")


def mostrarDatos(L1, L2): #D
    L1.reordenar('name')
    nombreEntrenador = str(input("\ningrese el nombre de un entrenador: "))
    entrenador = L1.obtener_elemento(L1.busqueda(nombreEntrenador,'name'))
    print ('Nombre: ',entrenador['name'],'| Torneos Ganados: ',entrenador['torneosGanados'],'| Batallas Ganadas: ',entrenador['ganadas'],'| Batallas Perdidas: ',entrenador['perdidas'])
    print('\n')
    for pokemon in entrenador['pokebals']:
        pokemon = L2.obtener_elemento(pokemon)
        print (pokemon['name'], '| Nivel: ', pokemon['level'],'| Tipo: ',pokemon['tipo'])


def porcentajes(L1): #E
    print ("Estos entrenadores ganaron mas del 79% de sus combates")
    for pos in range(0, L1.tamanio()):
        entrenador = L1.obtener_elemento(pos)
        total = ((entrenador['ganadas']) + (entrenador['perdidas']))
        winRate = ((entrenador['ganadas']) / (total))
        if (winRate >= 0.79):
            print (entrenador['name'], " ", "{0:.2f}".format(winRate*100) ," %")


def tipos(L1, L2): #F
    print ("\nEntrenadores cuyos pokemones son tipo Fuego/Planta o Agua/Volador")
    for pos in range(0,L1.tamanio()):
        entrenador = L1.obtener_elemento(pos)
        for posPokemon in entrenador['pokebals']:
            pokemon = L2.obtener_elemento(posPokemon)
            if ((pokemon['tipo'] == "Fuego") and (pokemon['subtype'] == "Planta")) or ((pokemon['tipo'] == "Agua") and (pokemon['subtype'] == "Volador")):
                print (entrenador['name'])


def promedioDeNivel(L1, L2): #G
    total = 0
    nEntrenador = str(input("Ingrese el nombre de un entrenador: "))
    pos = L1.busqueda(nEntrenador,'name')
    nEntrenador = L1.obtener_elemento(pos)
    cant = len(nEntrenador['pokebals'])
    for pos in nEntrenador['pokebals']:
        pokemon = L2.obtener_elemento(pos)
        total= total + pokemon['level']
    print ("Nivel Promedio de los pokemones", "{0:.2f}".format(total/cant))


def tieneXpokemon(L1, L2): #H
    cont = 0 
    pokemon = str(input("Ingrese el nombre de un pokemon: "))
    pokemon_busc = L2.busqueda(pokemon,'name')
    for pos in range(0,L1.tamanio()):
        entrenador = L1.obtener_elemento(pos)
        for i in entrenador['pokebals']:
            if i == pokemon_busc:
                cont+=1
    print ("Hay ",cont," que tienen un: ", pokemon)


def poke_repetidos(entrenadores): #I
    for pos in range(0, entrenadores.tamanio()):
        entrenador = entrenadores.obtener_elemento(pos)
        pokemon = entrenador['pokebals']
        for p in pokemon:
            if pokemon.count(p)>1:
                print ("El entrenador ",entrenador['name']," tiene pokemones repetidos")
                break


def funcion(entrenadores, pokemones): #J
    for pos in range(0, entrenadores.tamanio()):
        entrenador = entrenadores.obtener_elemento(pos)
        pokemon = entrenador['pokebals']
        for p in pokemon:
            pokemon = pokemones.obtener_elemento(p)
            if ( (pokemon['name']=="Tyrantrum") or (pokemon['name']=="Terrakion") or (pokemon['name']=="Wingull") ):
                print (entrenador['name']," tiene al menos un Tyrantrum/Terrakion/Wingull")


def busquedaDatos(entrenadores,pokemones,buscado1,buscado2):
    encontrado = False
    buscado1 = entrenadores.busqueda(buscado1,'name')
    buscado1 = entrenadores.obtener_elemento(buscado1)
    listPokemones = buscado1['pokebals']
    # obtencion de la lista de pokemones del entrenador 
    for element in listPokemones:
        pokemon = pokemones.obtener_elemento(element)
        if pokemon['name']== buscado2:
            encontrado = True
            break
    
    if encontrado==False:
        print (buscado1['name'],' NO tiene un ',buscado2)
    else:
        print (buscado1['name'],' tiene un ',buscado2)

    #obtencion del nombre del pokemon y su id


#armar_listas(EntrenadorES, PokemonES, entrenadores, pokemones)

#pokemonesEntrenador(entrenadores) #A

#torneos_Ganados(entrenadores) #B

#pokemonConHacks(entrenadores, pokemones) #C

#mostrarDatos(entrenadores, pokemones) #D

#porcentajes(entrenadores) #E

#tipos(entrenadores, pokemones) #F

#promedioDeNivel(entrenadores,pokemones) #G

#tieneXpokemon(entrenadores, pokemones) #H

#poke_repetidos(entrenadores) #I

"""
entrenador = str(input("\nIngrese un Entrenador: ")) #J
pokemon = str(input("Ingrese un Pokemon: "))
busquedaDatos(entrenadores,pokemones,entrenador,pokemon)

"""