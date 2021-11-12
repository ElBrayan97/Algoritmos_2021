from TDA_Lista import Lista

jedis = Lista()

Jedis = [
    {'name':'Luke Skywalker', 'main':"Obi-Wan Kenobi", 'saber':['Verde','Azul'], 'specie':'Humano'},
    {'name':'Yoda', 'main':"Desconocido", 'saber':['Verde'], 'specie':'Desconocido'},
    {'name':'Bastila Shan', 'main':"Qui-Gon Jinn", 'saber':['Amarillo'], 'specie':'Humano'},
    {'name':'Qui-Gon Jinn', 'main':"Conde Dooku", 'saber':['Verde'], 'specie':'Humano'},
    {'name':'Aayla Secura', 'main':'Quinlan Vos', 'saber':['Azul'], 'specie':'Twilek'},
    {'name':'Anakin Skywalker', 'main':'Qui-Gon Jinn', 'saber':['Azul'], 'specie':'Humano'},
    {'name':'Rey', 'main':'Luke Skywalker', 'saber':['Verde','Dorado'], 'specie':'Humano'},
    {'name':'Ahsoka Tano', 'main':'Anakin Skywalker', 'saber':['Verde','Amarillo','Azul'], 'specie':'Humano'},
    {'name':'Kit Fisto', 'main':'Yoda', 'saber':['Verde'], 'specie':'Nautolano'},
    {'name':'Mace Windu', 'main':'Yoda', 'saber':['Violeta'], 'specie':'Humano'},
    {'name':'Depa Billaba', 'main':'Mace Windu', 'saber':['Verde','Azul'], 'specie':'Humano'}
]

def armar_lista(Jedis,jedis):
    for jedi in Jedis:
        jedis.insertar(jedi,'name')
    print ("\nJedis: ")
    jedis.barrido()


def barridos_name_species(jedis): #A
    L2 = Lista()
    print ('\nJedis por nombre: ')
    for pos in range (0, jedis.tamanio()):
        jedi = jedis.obtener_elemento(pos)
        print (jedi['name'])
        L2.insertar(jedi,'specie')
    print("\nJedis por Especie: ")
    for pos in range(0, L2.tamanio()):
        jedi = L2.obtener_elemento(pos)
        print (jedi['specie'])


def  buscarYmostrar_info(jedis,name): #B
    jedi = jedis.obtener_elemento(jedis.busqueda(name,'name'))
    print ('\nNombre: ',jedi['name'])
    print ('Maestro: ',jedi['main'])
    print ('Colores de Sable: ',jedi['saber'])
    print ('Especie: ',jedi['specie'])


def buscarPadawan(jedis): #C
    print ("\n")
    for pos in range (0, jedis.tamanio()):
        jedi = jedis.obtener_elemento(pos)
        if (jedi['main'] == 'Yoda'):
            print (jedi['name']," es aprendiz de Yoda")
        elif (jedi['main'] == 'Luke Skywalker'):
            print (jedi['name']," es aprendiz de Luke Skywalker")


def humanosYotro(jedis):#D
    print ("\nHumanos y Twilek: ")
    for pos in range (0, jedis.tamanio()):
        jedi = jedis.obtener_elemento(pos)
        if jedi['specie']=="Humano":
            print (jedi['name']," es Humano")
        if jedi['specie']=="Twilek":
            print (jedi['name']," es Twilek")


def empiezanConA(jedis): #E
    print ("\nJedis que empiezan con A")
    for pos in range(0,jedis.tamanio()):
        jedi = jedis.obtener_elemento(pos)
        jedi = jedi['name']
        if (jedi[0:1])=='A':
            print (jedi)


def colores(jedis): #F y G
    print ("\nJedis que usaron sables de mas de un color: ")
    for pos in range(0, jedis.tamanio()):
        jedi = jedis.obtener_elemento(pos)
        sables = jedi['saber']
        if (len(sables))>1:
            print (jedi['name'])
        for sable in sables:
            if (sable=="Amarillo") or (sable == "Violeta"):
                print (jedi['name']," uso un sable Amarillo o Violeta")


def padawans(jedis):
    print ("\nPadawans de Qui-Gon Jinn y Mace Windu: ")
    for pos in range (0, jedis.tamanio()):
        jedi = jedis.obtener_elemento(pos)
        if (jedi['main']== "Qui-Gon Jinn"):
            print(jedi['name']," es discipulo de " ,jedi['main'])
        elif (jedi['main']== "Mace Windu"):
            print(jedi['name']," es discipulo de " ,jedi['main'])




armar_lista(Jedis,jedis)

#barridos_name_species(jedis) #A

#buscarYmostrar_info(jedis,'Ahsoka Tano') #B
#buscarYmostrar_info(jedis,'Kit Fisto')

#buscarPadawan(jedis) #C

#humanosYotro(jedis) #D

#empiezanConA(jedis) #E

#colores(jedis) #F

#padawans(jedis) #G
