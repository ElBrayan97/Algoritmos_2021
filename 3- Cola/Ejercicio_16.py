from TDA_Cola import Cola

C = Cola()

def cargarDocumento(C):
    A=["",0]
    A[0] = str(input("ingrese el nombre del documento: "))
    A[1] = int(input("Ingrese 1: Empleados, 2: Staff 3: Gerente   :"))
    C.arribo(A)


def ordenarPrioridad(cola):
    empleados = Cola()
    staff = Cola()
    gerente = Cola()

    while not cola.cola_vacia():
        A = cola.atencion()
        if A[1]==1:
            empleados.arribo(A)
        elif A[1]==2:
            staff.arribo(A)
        elif A[1]==3:
            gerente.arribo(A)

    while (not gerente.cola_vacia()):
        cola.arribo(gerente.atencion())

    while (not staff.cola_vacia()):
        cola.arribo(staff.atencion())

    while (not empleados.cola_vacia()):
        cola.arribo(empleados.atencion())

def imprimirDocumento(cola):
    print (cola.atencion()[0])


cargarDocumento(C) #Empleados
cargarDocumento(C) #Empleados
cargarDocumento(C) #Empleados 

cargarDocumento(C) #Staff
cargarDocumento(C) #Staff

cargarDocumento(C) #Gerente

ordenarPrioridad(C) #Se ordena la cola por prioridad

imprimirDocumento(C) #Se imprime el primer documento
imprimirDocumento(C) #Se imprime el segundo documento

cargarDocumento(C) #Se carga un documento de empleados
cargarDocumento(C) #Se carga un documento de empleados
cargarDocumento(C) #Se carga un documento de gerente

ordenarPrioridad(C) #Se ordena la cola por prioridad

while not C.cola_vacia(): # Se imprime toda la cola
    imprimirDocumento(C)
