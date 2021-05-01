class laberinto

def __init_(self)
    array = [[1, 1, 1, 1, 1, 2],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 2]]
    a = array
    x = 1
    y = 1

def mostrar(array)
    print(array[1,1])



"""
def resolver_laverinto(a, x, y):
    if (a[x][y] == 2) and (x <= 5) and (y <= 5):
        return salida()
    else:
        if (a[x][y] == 1) and (x <= 5) and (y <= 5):
            x = x+1
            return resolver_laverinto(a, x, y)
    elif (a[x-1][y] == 1):
        x = x-1
        return resolver_laverinto(a, x, y)
    elif (a[x][y+1] == 1):
        y = y+1
        return resolver_laverinto(a, x, y)
    elif (a[x][y-1] == 1):
        y = y-1
        return resolver_laverinto(a, x, y)

def salida():
    print('se salio del laverinto...')

resolver_laverinto(a, x, y)
print(x, y)
"""