from recursividad import *

print('Ej 1:')    # Ejercicio 1
num = int(input('Ingrese un numero: '))
for x in range(num):
    print('Fibbonacci: ', fib(x))


print('Ej 2:')
num = int(input('Ingrese un numero: '))  # Ejercicio 2
print('Suma: ', sum(num))


print('Ej 3:')
num = int(input('Ingrese un numero: '))  # Ejercicio 3
num2 = int(input('Ingrese otro numero: '))
print('Producto: ', prod(num, num2))


print('Ej 4:')
base = int(input('Ingrese un numero: '))  # Ejercicio 4
exp = int(input('Ingrese otro numero: '))
print('Potencia: ', pot(base, exp))


print('Ej 5:')
cadena = (input('Ingrese una secuencia de numeros: '))  # Ejercicio 5
print('Secuencia Invertida: ', invert(cadena))


print('Ej 6:')
num = int(input('Ingrese un numero: '))  # Ejercicio 6
print('Serie: ', serie(num))


print('Ej 7:')
num = int(input('Ingrese un numero: '))  # Ejercicio 7
print('Decimal a Binario: ', invertDecaBin(num))


print('Ej 8:')
print ('INGRESE NUMEROS PARA CALCULAR SU LOGARTMO')
num = int(input('Ingrese un numero: '))  # Ejercicio 8 No Funciona!
num2 = int(input('Ingrese la base: '))
log  =  (logaritmo(num, num2))
print('Logaritmo: ',log)


print('Ej 9: ')
n = int(input('Ingrese un Numero: '))  # Ejercicio 9
ac = int(0)
print('Cantidad de digitos del numero: ', cont(n, ac))

print('Ej 10:')
num = int(input('Ingrese un Numero: '))  # Ejercicio 10
pos = int(input('cantidad de digitos del numero: '))
pos = pos-1
print('Inversion: ', inversion(num, pos))

print('Ej 11:')
n = int(input('ingrese un numero: '))
n2 = int(input('ingrese un numero: '))
print('MCD: ', mcd(n, n2))
