participantes ={}

print("Menu principal")
cantidad=int(input("Ingrese la cantidad de participantes: "))
for i in range(cantidad):
    print(f"\nIngrese los datos de participante: {i+1}")
    numeroDorsal=int(input("Ingrese el numero de dorsal: "))
    participantes[numeroDorsal] = {}

    participantes[numeroDorsal]["nombre"]=input("Ingrese el nombre del dorsal: ")
    participantes[numeroDorsal]["edad"]=int(input("Ingrese el edad: "))
    participantes[numeroDorsal]["categoria"]=input("Ingrese el categoria: ")


def quick_sorter(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores =[x for x in lista[1:] if x[1]["edad"] <= pivote[1]["edad"]]
    mayores= [x for x in lista[1:] if x[1]["edad"] > pivote[1]["edad"]]

    return quick_sorter(menores) + [pivote] + quick_sorter(mayores)

lista_participantes =list(participantes.items())



