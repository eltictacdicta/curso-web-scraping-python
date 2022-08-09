#try - except
nueva_lista=[2,6,7, "Mexico"]

for elemento in nueva_lista:
    try:
        print(elemento/2)
    except:
        print('El elemnto no es un numero!')